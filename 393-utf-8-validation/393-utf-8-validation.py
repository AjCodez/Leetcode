class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i=0
        while i<len(data):
            if len(str(bin(data[i]))[2:])<8:
                i+=1
            elif str(bin(data[i]))[2:][0:3]=='110' and len(str(bin(data[i]))[2:])==8:
                if i+1!=len(data) and str(bin(data[i+1]))[2:][0:2]=='10' and len(str(bin(data[i+1]))[2:])==8:
                    i+=2
                else:
                    return False
            elif str(bin(data[i]))[2:][0:4]=='1110' and len(str(bin(data[i]))[2:])==8:
                if i+2<len(data) and str(bin(data[i+1]))[2:][0:2]=='10' and len(str(bin(data[i+1]))[2:])==8 and str(bin(data[i+2]))[2:][0:2]=='10' and len(str(bin(data[i+2]))[2:])==8:
                    i+=3
                else:
                    return False
            elif str(bin(data[i]))[2:][0:5]=='11110' and len(str(bin(data[i]))[2:])==8:
                if i+3<len(data) and str(bin(data[i+1]))[2:][0:2]=='10' and len(str(bin(data[i+1]))[2:])==8 and str(bin(data[i+2]))[2:][0:2]=='10' and len(str(bin(data[i+2]))[2:])==8 and str(bin(data[i+3]))[2:][0:2]=='10' and len(str(bin(data[i+3]))[2:])==8:
                    i+=4
                else:
                    return False
            else:
                return False
        return True