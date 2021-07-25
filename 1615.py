# 1615. Maximal Network Rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = [[] for _ in range(n)]

        for fr, to in roads:
            network[fr].append(to)
            network[to].append(fr)

        maxrank = 0
        for i in range(len(network)):
            city1rank = len(network[i])
            if city1rank > 0:
                for j in range(i + 1, len(network)):
                    this_rank = city1rank + len(network[j]) - (i in network[j])
                    maxrank = max(maxrank, this_rank)

        return maxrank
        
        
        
 # v2
         dnetwork = defaultdict(list)

        for fr, to in roads:
            dnetwork[fr].append(to)
            dnetwork[to].append(fr)

        cities = sorted(dnetwork.keys())
        maxrank = 0
        for i in range(len(cities)):
            city1rank = len(dnetwork[cities[i]])
            for j in range(i + 1, len(cities)):
                this_rank = city1rank + len(dnetwork[cities[j]]) - (cities[i] in dnetwork[cities[j]])
                maxrank = max(maxrank, this_rank)

        return maxrank
