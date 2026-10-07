class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        sml_str = strs[0]
        for string in strs[1:]:
            if len(string) < len(sml_str):
                sml_str = string

        start = len(sml_str)

        dic = {

        }

        while (start >= 0):
            for string in strs:
                if string[:start + 1] in dic:
                    dic[string[:start + 1]] += 1

                elif string[:start + 1] not in dic:
                    dic[string[:start + 1]] = 1

            if (len(dic) > 1) :
                start -= 1
                dic = {
                }

            if len(dic) == 1:
                return str(dic.keys())[12:-3]

        

        return ""

        