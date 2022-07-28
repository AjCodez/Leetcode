def getSS(s):
    if s=='':
        return ['']
    cc=s[0]
    ss=s[1:]
    tres=getSS(ss)
    res = []
    for i in tres:
        res.append(i)
        res.append(cc+i)
        res.append(str(ord(cc))+i)
            
    return res
print(getSS('abc'))