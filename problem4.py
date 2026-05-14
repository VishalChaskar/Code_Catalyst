from collections import deque
 
def is_valid(s):
    return "CC" not in s
 
def solve(start, end):
    chars = ['A', 'B', 'C']
    queue = deque([start])
    distance = {start: 0}
    ways = {start: 1}
    while queue:
        curr = queue.popleft()
        for i in range(len(curr)):
            for ch in chars:
                if curr[i] == ch:
                    continue
                new_str = curr[:i] + ch + curr[i+1:]
                if not is_valid(new_str):
                    continue
                if new_str not in distance:
                    distance[new_str] = distance[curr] + 1
                    ways[new_str] = ways[curr]
                    queue.append(new_str)
                elif distance[new_str] == distance[curr] + 1:
                    ways[new_str] += ways[curr]
    return distance.get(end, -1), ways.get(end, 0)
 
 
start = "CBAB"
end = "ABCB"
 
length, paths = solve(start, end)
 
print("Length:", length)
print("Paths:", paths)