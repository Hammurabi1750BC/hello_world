# 1487	Making File Names Unique

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d_names = dict()
        
        for name in names:
            if name in d_names.keys():
                num = d_names[name] + 1
                
                while name + '(' + str(num) + ')' in d_names.keys():
                    num += 1
                
                d_names[name] = num
                name += '(' + str(num) + ')'
                
            d_names[name] = 0
            
        return d_names.keys()
