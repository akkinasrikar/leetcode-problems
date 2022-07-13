class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hashmap={}
        def add(domain):
            n,d=domain.split(" ")
            n,d=int(n),d.split(".")
            while d:
                sub=".".join(d)
                if sub not in hashmap: hashmap[sub] = n
                else: hashmap[sub] += n
                d.pop(0)
        for dm in cpdomains:
            add(dm)
        res=[]
        for key in hashmap:
            ans=" ".join([str(hashmap[key]),key])
            res.append(ans)
        return res