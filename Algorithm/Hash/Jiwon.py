# ---- 개별 체이닝을 통한 해시 맵 구현 ---- #

# 체이닝 노드 생성 및 초기화
class ChainingHash:
    # key, value: 임의의 자료형
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.next = None

# 해시 맵 구현
class MyHashMap:
    def __init__(self):
        self.size = 1000 # 적당한 크기로 임의 설정
        self.table = [None] * self.size # 기본 슬롯은 모두 None
        

    def put(self, key: int, value: int) -> None:
        hashValue = key % self.size # 문제에서 사용할 기본 해시 연산

        # 슬롯이 비어있을 경우 (key, value) pair를 삽입 후 종료
        if self.table[hashValue] is None:
            self.table[hashValue] = ChainingHash(key, value)
            return
        
        # 슬롯이 비어있지 않은 경우(is not None)
        tmp = self.table[hashValue]
        while tmp:
            # 이미 동일한 키가 존재하는 경우 값을 업데이트하고 종료
            if tmp.key == key:
                tmp.value = value
                return
            # 동일한 키도 발견하지 못하고 연결 리스트 탐색을 끝낸 경우
            if tmp.next is None:
                # 연결 리스트의 마지막에 pair를 연결해줌
                tmp.next = ChainingHash(key, value)
                return
            tmp = tmp.next
        

    def get(self, key: int) -> int:
        hashValue = key % self.size # 문제에서 사용할 기본 해시 연산

        # 슬롯이 비어있을 경우
        if self.table[hashValue] is None:
            return -1
        
        # 슬롯이 비어있지 않은 경우(is not None)
        tmp = self.table[hashValue]
        while tmp:
            if tmp.key == key:
                return tmp.value
            tmp = tmp.next # 키가 일치하지 않는다면 연결 리스트를 돌며 탐색
        return -1 # 탐색의 끝까지 일치하는 key를 찾지 못했을 경우


    def remove(self, key: int) -> None:
        hashValue = key % self.size # 문제에서 사용할 기본 해시 연산
        
        # 삭제할 슬롯이 없는 경우 그냥 종료
        if self.table[hashValue] is None:
            return

        # 삭제할 슬롯이 존재하는 경우(is not None)
        tmp = self.table[hashValue]
        # 삭제 대상이 슬롯의 첫번째 노드인 경우
        if tmp.key == key:
            self.table[hashValue] = tmp.next
            return

        # 첫번째 노드와 key가 일치하지 않는 경우 탐색을 진행하여 삭제
        else:
            while tmp.next:
                # 다음 노드의 key 값이 삭제할 key 값과 일치할 경우 반복 탈출
                if tmp.next.key == key:
                    break
                tmp = tmp.next

            # 1. tmp.next is None: 삭제할 노드 발견 못함
            if tmp.next is None:
                return
            # 2. 삭제 대상 노드 발견 (tmp.next)
            else: tmp.next = tmp.next.next
            return
