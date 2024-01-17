class Solution:
    def arrangeWords(self, text: str) -> str:
        words = list(text.lower().split())
        words.sort(key=lambda x: len(x))
        return " ".join(words).capitalize()
