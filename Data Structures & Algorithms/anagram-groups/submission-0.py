class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs :
            return []
        if len(strs) == 1 :
            return [strs]
        output = {}
        for i in strs :
            key = "".join(sorted(i))
            output[key] = output.get(key , [] ) + [i]
        return list(output.values())

        