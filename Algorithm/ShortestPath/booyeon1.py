class Solution(object):

    def networkDelayTime(self, times, n, k):

        # 최단경로표에서 가장 큰값 출력'

        times.sort()

        record = {}

        for i in range(n):

            record.update({i+1:float('inf')})

        queue = deque([k])

        record[k] = 0

        while queue:
            print(queue)

            crr = queue.popleft()

            for route in times:

                if route[0] == crr:
                    if record[route[1]] > record[crr] + route[2]:
                        queue.append(route[1])

                        record[route[1]] = record[crr] + route[2]


        depth = max(record.values())

        return depth if depth != float('inf') else -1