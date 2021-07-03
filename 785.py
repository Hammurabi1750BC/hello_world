# 785	Is Graph Bipartite?
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # q
        ab = [0] * len(graph)  # set a = 1, b = -1

        for i in range(len(graph)):
            if ab[i] == 0:
                ab[i] = 1
                q = deque([i])
                while q:
                    node = q.pop()
                    for neigh in graph[node]:
                        if ab[neigh] == 0:
                            ab[neigh] = ab[node] * -1
                            q.append(neigh)

                        if ab[neigh] == ab[node]:
                            return False

        return True

        # dfs

        def recurse2neighbors(i, ab):
            if i in dab:
                return dab[i] == ab

            dab[i] = ab
            for nei in graph[i]:
                if not recurse2neighbors(nei, 1 - ab):
                    return False

            return True

        dab = dict()  # dict of a or b  0 for set a, 1 for set b

        for i in range(len(graph)):
            if i not in dab:
                if not recurse2neighbors(i, ab=0):
                    return False

        return True
