class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)

        while heap:
            occ, letter = heapq.heappop(heap)
            if occ == 0:
                break

            if len(res) > 1 and res[-1] == letter and res[-2] == letter:
                if not heap:
                    break

                occ2, letter2 = heapq.heappop(heap)
                if occ2 == 0:
                    break

                res.append(letter2)
                if occ2 < -1:
                    heapq.heappush(heap, (occ2+1, letter2))

                heapq.heappush(heap, (occ, letter))

            else:
                res.append(letter)
                if occ < -1:
                    heapq.heappush(heap, (occ+1, letter))

        return ''.join(res)