# 791	Custom Sort String

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        c_str = Counter(str)
        
        custom_sorted = ''
        for char in order:
            if char in c_str:
                custom_sorted += char * c_str.pop(char)
        
        for char in c_str:
            custom_sorted += char * c_str[char]
        
        return custom_sorted
    
    # v1
    def customSortString(self, order: str, str: str) -> str:
        counter_str = Counter(str)
        
        sorted_string = ''
        for char in order:
            if char in counter_str:
                sorted_string += char * counter_str[char]
        
        remainder = set(counter_str.keys()).difference(order)
        for char in remainder:
            sorted_string += char * counter_str[char]

        return sorted_string
