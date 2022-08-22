class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            ip=queryIP.split(".")
            if len(ip)!=4:
                return "Neither"
            for i in ip:
                try:
                    if str(int(i))!=i:
                        return "Neither"
                except:
                    return "Neither"
                if not i.isnumeric() or int(i)<0 or int(i)>255:
                    return "Neither"
            return "IPv4"
        ip=queryIP.split(":")
        if len(ip)!=8:
            return "Neither"
        for i in ip:
            if len(i)<1 or len(i)>4 :
                return "Neither"
            try:
                a=int(i,16)
            except:
                return "Neither"
        return "IPv6"
        