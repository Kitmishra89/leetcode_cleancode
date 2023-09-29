class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dix = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in dix:
                dix[s].append(i)
            else:
                dix[s] = [i]

        return dix.values()

