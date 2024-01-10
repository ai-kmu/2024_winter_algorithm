class MyHashMap(object):

    def __init__(self):
        self.hashMap = []
        

    #get index 
    #return index by key
    def getIndex(self, key):
        """
        :type key: int
        :rtype: int
        """
        result =-1

        for hmi in range(len(self.hashMap)):
            if self.hashMap[hmi][0] == key:
                    result = hmi
            #대규모 데이터 검색속도 향상을 위한 부분
            #if(self.hashMap[hmi][0] > key):#key를 넘어가면 break
            #    break

        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.getIndex(key)
        if (index<0): #hashMap내에 같은 key가 없을때
            self.hashMap.append([key,value])
            #self.hashMap.sort() #대규모 데이터 검색속도 향상을 위한 정렬(데이터 갱신때 정렬) 
        else: #hashMap내에 같은 key가 있을때 
            if len(self.hashMap[index]) > 1:
                self.hashMap[index][1] = value
        



        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.getIndex(key)
        return index if index == -1 else self.hashMap[index][1] #value return

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.getIndex(key)
        try:
            if index == -1 : raise IndexError
            self.hashMap.pop(index)
        except IndexError:
            print("fail to remove. please check your key")



# Your MyHashMap object will be instantiated and called as such:
#obj = MyHashMap()
#obj.put(11,0)
#print(obj.hashMap)
#print(obj.get(11))
# param_2 = obj.get(key)
# obj.remove(key)