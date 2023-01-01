class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        RUNTIME: 29 ms (91.56%)
        MEMORY: 13.8 MB (74.33%)
        """
        if len(pattern) != len(s.split()): return False
        dict_ = {}
        for key, value in zip(pattern, s.split()):
            if key not in dict_:
                if value in dict_.values():
                    return False
                dict_[key] = value
            elif dict_[key] != value:
                return False
        return True
