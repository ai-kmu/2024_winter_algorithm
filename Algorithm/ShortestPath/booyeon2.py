class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # graph init
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        # record init
        record = {}
        for i in range(n):
            record[i] = float('inf')
        record[src] = 0
        
        # BFS
        queue = deque([(src, 0, 0)])  # (city, cost, stops)
        while queue:
            city, cost, stops = queue.popleft()
            if city == dst:  # 도착확인
                continue
            if stops > k: 
                continue
            for neighbor, price in graph[city]:
                new_cost = cost + price
                if new_cost < record[neighbor]:
                    record[neighbor] = new_cost
                    queue.append((neighbor, new_cost, stops + 1))
        
        return record[dst] if record[dst] != float('inf') else -1