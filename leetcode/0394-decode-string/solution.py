class Solution(object):
    def decodeString(self, s):
        """
        RUNTIME: 37 ms (66.69%)
        MEMORY: 14 MB (20.26%)
        """
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                continue
            if s[i] != ']':
                stack.append(s[i])
            else:
                local = ''
                while stack:
                    cur = stack.pop()
                    if cur == '[':
                        count = ''
                        while stack:
                            n = stack.pop()
                            if not n.isnumeric():
                                stack.append(n)
                                break
                            count = n + count
                        local *= int(count)
                        stack.extend([c for c in local])
                        break
                    local = cur + local
        return ''.join(stack)
