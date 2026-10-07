class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {

        }
        
        for index,string in enumerate(strs):
            if str(sorted(string)) not in strings:
                strings[str(sorted(string))] = [index]

            elif str(sorted(string)) in strings:
                strings[str(sorted(string))].append(index)


        result = []

        for indices in strings.values():

            i = []

            for index in indices:
                i.append(strs[index])
            
            result.append(i)
            

        return result

          