class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
'''
encode(list):
    string = ''
    for i in list:
        string += i
        string += ' '

    return string

decode(string):
    list = []
    word = ''
    for i in range(0, len(string) - 1):
        if (string[i] == " " or i == len(string) - 1):
            list.append(word)
            word = ""
            continue

        word += string[i]

    return list
'''