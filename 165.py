# 165	Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(x) for x in version1.split('.')]
        version2 = [int(x) for x in version2.split('.')]
        
        for i in range(max(len(version1), len(version2))):
            v1 = 0 if i >= len(version1) else version1[i]
            v2 = 0 if i >= len(version2) else version2[i]
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0
