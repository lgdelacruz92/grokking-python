class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        self.adj_list = {
            1: [2, 4, 5, 6, 8],
            2: [1, 3, 4, 5, 6, 7, 9],
            3: [2, 5, 6, 4, 8],
            4: [1, 2, 5, 8, 7, 3, 9],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [2, 3, 5, 8, 9, 1, 7],
            7: [4, 5, 8, 2, 6],
            8: [4, 5, 6, 7, 9, 1, 3],
            9: [5, 6, 8, 2, 4]
        }

        def backtrack(node, path, d, paths, visited):
            if len(path) == d:
                paths.append(path[:])
                return
            
            # manually add the exceptions if the conditions are met
            if node == 2 and 5 in path:
                self.adj_list[node].append(8)
            if node == 8 and 5 in path:
                self.adj_list[node].append(2)
            if node == 4 and 5 in path:
                self.adj_list[node].append(6)
            if node == 6 and 5 in path:
                self.adj_list[node].append(4)
            if node == 1 and 2 in path:
                self.adj_list[node].append(3)
            if node == 3 and 2 in path:
                self.adj_list[node].append(1)
            if node == 3 and 6 in path:
                self.adj_list[node].append(9)
            if node == 9 and 6 in path:
                self.adj_list[node].append(3)
            if node == 7 and 8 in path:
                self.adj_list[node].append(9)
            if node == 9 and 8 in path:
                self.adj_list[node].append(7)
            if node == 1 and 4 in path:
                self.adj_list[node].append(7)
            if node == 7 and 4 in path:
                self.adj_list[node].append(1)
            if node == 1 and 5 in path:
                self.adj_list[node].append(9)
            if node == 9 and 5 in path:
                self.adj_list[node].append(1)
            if node == 3 and 5 in path:
                self.adj_list[node].append(7)
            if node == 7 and 5 in path:
                self.adj_list[node].append(3)

            # backtracking
            for next_node in self.adj_list[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    path.append(next_node)
                    backtrack(next_node, path, d, paths, visited)
                    path.pop()
                    visited.remove(next_node)

            # cleanup appended exception
            if node == 2 and 5 in path:
                self.adj_list[node].pop()
            if node == 8 and 5 in path:
                self.adj_list[node].pop()
            if node == 4 and 5 in path:
                self.adj_list[node].pop()
            if node == 6 and 5 in path:
                self.adj_list[node].pop()
            if node == 1 and 2 in path:
                self.adj_list[node].pop()
            if node == 3 and 2 in path:
                self.adj_list[node].pop()
            if node == 3 and 6 in path:
                self.adj_list[node].pop()
            if node == 9 and 6 in path:
                self.adj_list[node].pop()
            if node == 7 and 8 in path:
                self.adj_list[node].pop()
            if node == 9 and 8 in path:
                self.adj_list[node].pop()
            if node == 1 and 4 in path:
                self.adj_list[node].pop()
            if node == 7 and 4 in path:
                self.adj_list[node].pop()
            if node == 1 and 5 in path:
                self.adj_list[node].pop()
            if node == 9 and 5 in path:
                self.adj_list[node].pop()
            if node == 3 and 5 in path:
                self.adj_list[node].pop()
            if node == 7 and 5 in path:
                self.adj_list[node].pop()

            
        paths = []
        visited = set()
        for i in range(1, 10):
            for d in range(m, n+1):
                visited.add(i)
                backtrack(i, [i], d, paths, visited)
                visited.remove(i)


        return len(paths)
                