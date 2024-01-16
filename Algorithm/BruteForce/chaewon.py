class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        words = list(text.split(" "))
        words.sort(key=lambda x: len(x))
        return " ".join(words).capitalize()
