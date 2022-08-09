class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        start=97
        hashmap={}
        for i in key:
            if i!=" " and i not in hashmap:
                hashmap[i]=chr(start)
                start += 1
        res=""
        for i in message:
            if i==" ": res += " "
            else: res +=hashmap[i]
        return res