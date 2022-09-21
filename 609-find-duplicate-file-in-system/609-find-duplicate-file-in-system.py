class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap={}
        for i in range(len(paths)):
            temp=paths[i].split(" ")
            #print(temp)
            for j in range(1,len(temp)):
                w=temp[j].split("(")
                a=w[1][:-1]
                b=w[0]
                if a not in hashmap:
                    hashmap[a]=[[temp[0],b]]
                else:
                    hashmap[a].append([temp[0],b])
        res=[]
        for i in hashmap:
            x=[]
            if len(hashmap[i])<2:
                continue
            for j in hashmap[i]:
                x.append(j[0]+"/"+j[1])
            res.append(x)
        return res