class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            nodes = []

            while stack:
                node = stack.pop()
                nodes.append(node)

                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        stack.append(neighbour)

            size = len(nodes)
            complete = True

            for node in nodes:
                if len(graph[node]) != size - 1:
                    complete = False
                    break

            if complete:
                answer += 1

        return answer
        