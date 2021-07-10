    def countTriples(self, n: int) -> int:
        squares = 0
        square_list = [x ** 2 for x in range(1, n + 1)]
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a != b and a ** 2 + b ** 2 in square_list:
                    squares += 1

        return squares

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        visited.add((entrance[0], entrance[1]))

        heap = [[0, entrance[0], entrance[1]]]  # steps, row, col

        while heap:
            steps, row, col = heapq.heappop(heap)

            if [row, col] != entrance:
                if row in [0, len(maze) - 1] or col in [0, len(maze[0]) - 1]:
                    return steps

            for nei in [[-1, 0],
                        [0, -1], [0, 1],
                        [1, 0]]:
                nr, nc = row + nei[0], col + nei[1]

                if (nr, nc) not in visited and 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != '+':
                    visited.add((nr, nc))
                    heapq.heappush(heap, [steps + 1, nr, nc])
        return -1
