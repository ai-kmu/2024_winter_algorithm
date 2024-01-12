class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.map = [-1 for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1
