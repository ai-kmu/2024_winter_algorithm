class Solution(object):
    def arrangeWords(self, text):
        lst = list(text.lower().split(" "))
        lst.sort(key=len)
        lst = " ".join(lst).capitalize()
        return lst
        """
        :type text: str
        :rtype: str
        """
