class Solution:
    # def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
    #     if target == startFuel:
    #         return 0
    #     fs=0
    #     arr1=[]
    #     arr2=[]
    #     sp=0
    #     for i in stations:
    #         j,k=i
    #         while j<=startFuel:
    #             arr1.append(j)
    #             arr2.append(k)
    #         mfuel=[]
    #         for l in range(sp,len(arr1)):
    #             mfuel.append()
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        for i in stations:
            i.append(True)
        fuel_stations=list(sorted(stations,key=lambda x : x[1],reverse=True))
        ans=0
        maxReachable=startFuel
        if maxReachable>=target:
            return 0
        while(True):
            flag=0
            for i in fuel_stations:
                if i[0]<=maxReachable and i[2]:
                    flag=1
                    i[2]=False
                    ans+=1
                    maxReachable+=i[1]
                    break
            if maxReachable>=target:
                return ans
            if flag==0:
                return -1
        return -1