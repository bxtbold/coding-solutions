class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        RUNTIME: 3186 ms (11.12%)
        MEMORY: 15 MB (95.22%)
        """
        if '0000' in deadends: return -1
        # initialize
        queue, visited = ['0000'], {'0000'}
        step = 0
        # bfs
        while len(queue) != 0:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur == target:
                    return step
                neighbors = self.get_neighbors(cur)
                # iterate through all neighbors
                for j in neighbors:
                    if j in visited or j in deadends:
                        continue
                    queue.append(j)
                    visited.add(j)
            step += 1
        return -1

    def get_neighbors(self, cur):
        neighbors = {}
        for move in ['0001', '0010', '0100', '1000']:
            # plus
            next_move = ''
            for i in range(4):
                next_move += str((int(cur[i]) + int(move[i])) % 10)
            neighbors[next_move] = 1
            # minus
            next_move = ''
            for i in range(4):
                tmp = (int(cur[i]) - int(move[i])) % 10
                next_move += str(tmp) if tmp != -1 else '9'
            neighbors[next_move] = 1
        return neighbors
