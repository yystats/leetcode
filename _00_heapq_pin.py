import heapq

def create_pins(pins: list[int], k: int) -> list[list[int]]:
    # save (height, column)
    heap = [(0, i) for i in range(k)]
    columns = [[] for _ in range(k)]

    for pin in pins:
        height, col = heapq.heappop(heap)
        columns[col].append(pin)
        heapq.heappush(heap, (height + pin, col))

    return columns

pins = [1,2,3,4,5,6]
k = 3
print(create_pins(pins, k))

