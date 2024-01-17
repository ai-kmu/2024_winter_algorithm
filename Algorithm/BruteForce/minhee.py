class Solution:
    def arrangeWords(self, text: str) -> str:
        tmp = text.split(' ')
        tmp.sort(key=len)
        result = ' '.join(tmp)
        result = result.capitalize()

        return result
        
