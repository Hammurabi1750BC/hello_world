# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        orig_fc = [x for x in favoriteCompanies]
        favoriteCompanies.sort(key = lambda x: len(x), reverse=True)
        
        not_sub = []
        
        for i, sub_list in enumerate(favoriteCompanies):
            this_not_sub = True
            
            for longer_sub_list in favoriteCompanies[:i]:
                if len(sub_list) < len(longer_sub_list):
                    diff = set(sub_list).difference(set(longer_sub_list))
                    if not diff:
                        this_not_sub = False
                        break
                else:
                    break   # can be a subset only if list is longer
            if this_not_sub:
                not_sub.append(orig_fc.index(favoriteCompanies[i]))
            
        return sorted(not_sub)
