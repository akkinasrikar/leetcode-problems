class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def isIpv4(ip):
            try: return str(int(ip))==ip and 0<=int(ip)<=255
            except: return False
        
        def isIpv6(ip):
            try: return len(ip)<=4 and int(ip,16)>=0
            except: return False
        
        if queryIP.count(".")==3 and all(isIpv4(i) for i in queryIP.split(".")):
            return "IPv4"
        if queryIP.count(":")==7 and all(isIpv6(i) for i in queryIP.split(":")):
            return "IPv6"
        return "Neither"