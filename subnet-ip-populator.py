import sys

def isSubnet(str):
	return str.find("/") > -1
def ipToInt(ip):
	v = 0
	for n in map(int, ip.split(".")):
		v = v << 8 | n
		#print("ipToInt", ip, v)
	#print("ipToInt result", ip, v)
	return v 
def intToIp(i):
	nums = list();
	for n in range(24, -1, -8):
		nums.append(0xff & (i >> n))
	return ".".join(map(str, nums))
def maskOf(subnet):
	return 0xffffffff << (32 - int(subnet))
			
def nicAssignable(ip):
	for n in range(0, 24, 8):
		i = ip >> n & 0xff
		if i == 0 or i == 0xff: # 0 or 255
			return False
	return True

def subnetRange(str):
	if not isSubnet(str):
		return (str,)
	else:
		i = str.index("/")
		base = str[:i]
		subnet = str[i+1:]
		mask = maskOf(subnet)
		b = ipToInt(base) & mask
		s = b + 1
		e = (b | (0xffffff & ~mask)) 
		return map(intToIp, filter(nicAssignable, range(s, e)) if s < e else ())
while True:
	line = sys.stdin.readline().strip()
	if not line or len(line) == 0:
		break
	for ip in subnetRange(line):
		print(ip)

