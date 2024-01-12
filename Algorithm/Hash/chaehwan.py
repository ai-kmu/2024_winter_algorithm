from collections import defaultdict

class ListNode:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.next= None

class MyHashMap(object):

    def __init__(self):
        self.myMap = defaultdict(ListNode)
        self.MAX_SIZE = 10**3

    def put(self, key, value):
        idx = key%self.MAX_SIZE
        if self.myMap[idx].value is None:
            self.myMap[idx] = ListNode(key, value)
            return
        p = self.myMap[idx]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
               break
            p = p.next

        p.next = ListNode(key, value)
        

    def get(self, key):
        idx = key%self.MAX_SIZE
        if self.myMap[idx].value is None:
           return -1

        p = self.myMap[idx]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        
    def remove(self, key):
        idx = key%self.MAX_SIZE
        if self.myMap[idx].value is None:
            return -1
        p = self.myMap[idx]
        if p.key == key:
            if p.next is None: #다음 노드가 없으면 해당 인덱스를 빈 리스트 노드로 초기화
                self.myMap[idx] = ListNode()
            else:  # 다음 노드가 있으면 다음노드를 시작노드로 설정
                self.myMap[idx] = p.next
            return
        # 위에서 처음 노드가 해당 key일 때 리턴시킴으로써 아래에서는 처음 iter에서 key값이 같을리가 없음
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

#myHashMap = MyHashMap()
#myHashMap.put(1, 1); # The map is now [[1,1]]
#myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
#myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
#myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
#myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
#print(myHashMap.myMap[2].value)
#myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
#myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
#myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]
