class Solution(object):
    """
        :type text: str
        :rtype: str
    """
    def arrangeWords(self, text):
        result = []

        lenNum = [0]*50 #단어 길이별 현재 result에 저장된 단어 갯수

        textList = text.split()
        textList[0]=textList[0].lower() #대문자 풀기
        
        #단어 길이별 정렬
        for word in textList:
            wordLen = len(word)#단어 길이

            result.insert(sum(lenNum[:wordLen]),word)
            lenNum[wordLen-1] += 1

        result[0] = ''.join( [result[0][0].upper(), result[0][1:]] ) #첫 알파벳 대문자로

        return ' '.join(result)