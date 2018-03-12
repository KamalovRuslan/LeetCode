class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph) - 1
        paths = [[0]]
        idxs = [(i, p[-1]) for i, p in enumerate(paths)]
        added = [node for idx in idxs for node in graph[idx[1]]]
        while min(added) < n:
            paths = [paths[idx[0]] + [node] if node else paths[idx[0]] \
                           for idx in idxs for node in graph[idx[1]]]
            added = [node for idx in idxs for node in graph[idx[1]]]
            idxs = [(i, p[-1]) for i, p in enumerate(paths)]
        return paths


if __name__ == "__main__":
    graph = eval(input())
    solution = Solution()
    print(solution.allPathsSourceTarget(graph))
