class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for pre, post in prerequisites:
            if pre in adj.keys():
                adj[pre].append(post)
            else:
                adj[pre] = [post]

        for key in adj.keys():
            visited = set()
            if self.detect_cycle(key, adj, visited):
                return False
        return True

    def detect_cycle(self, start, adj, visited):
        if start not in adj.keys():
            return False
        visited.add(start)
        for node in adj[start]:
            if node in visited:
                return True
            if self.detect_cycle(node, adj, visited):
                return True
        visited.remove(start)
        return False