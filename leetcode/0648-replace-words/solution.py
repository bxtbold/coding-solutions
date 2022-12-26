class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        RUNTIME: 99 ms (97.3%)
        MEMORY: 23.6 MB (23.6%)
        """
        dictionary = set(dictionary)
        # find longest root
        longest = 0
        for i in dictionary:
            longest = max(longest, len(i))

        # replace
        result = ''
        trigger = False
        for word in sentence.split():
            each = ''
            count = 0
            for char in word:
                each += char
                count += 1
                if each in dictionary:
                    result += ' ' + each
                    trigger = True
                    break
                if count > longest:
                    break
            if trigger:
                trigger = False
            else:
                result += ' ' + word
        return result.strip()
