class Solution:
    def arrangeWords(self, text: str) -> str:
        list = text.split()
        list.sort(key=len)

        answer = " ".join(list)
        answer = answer.lower()
        answer = answer.capitalize()

        return answer
