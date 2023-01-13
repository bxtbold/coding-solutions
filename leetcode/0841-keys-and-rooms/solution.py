class NonRecursiveSolution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        RUNTIME: 67 ms (91.79%)
        MEMORY: 14.4 MB (53.2%)
        """
        visited = set()
        visited.add(0)
        stack = [0]
        while stack:
            current = stack.pop()
            for child in rooms[current]:
                if child not in visited:
                    visited.add(child)
                    stack.append(child)
        return len(visited) == len(rooms)


class RecursiveSolution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        RUNTIME: 71 ms (84.27%)
        MEMORY: 14.9 MB (23.32%)
        """
        def dfs(current, parent):
            visited.add(current)
            for child in rooms[current]:
                if child == parent or child in visited:
                    continue
                dfs(child, parent)
        visited = set()
        visited.add(0)
        dfs(0, -1)
        return len(visited) == len(rooms)
