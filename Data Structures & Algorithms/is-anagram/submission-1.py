class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        length2 = len(t)
        myDict = {}
        myDict2 = {}
        for i in range(length):
            if (s[i] in myDict):
                myDict[s[i]] += 1
            else:
                myDict[s[i]] = 1

        for i in range(length2):
            if (t[i] in myDict2):
                myDict2[t[i]] += 1
            else:
                myDict2[t[i]] = 1

        return myDict == myDict2