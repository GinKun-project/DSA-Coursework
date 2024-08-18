from collections import deque

def can_be_friends_bfs(graph, restrictions, u, v):
   
    for x, y in restrictions:
        if (u == x and v == y) or (u == y and v == x):
            return False
        
      
        queue = deque([x])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node == y:
                return False
            for neighbor in graph[node]:
                queue.append(neighbor)
    return True

def friend_requests_bfs(num_houses, restrictions, requests):
    graph = {i: [] for i in range(num_houses)}
    result = []

    for u, v in requests:
        if can_be_friends_bfs(graph, restrictions, u, v):
            graph[u].append(v)
            graph[v].append(u)
            result.append("approved")
        else:
            result.append("denied")
    
    return result


num_houses1 = 3
restrictions1 = [[0, 1]]
requests1 = [[0, 2], [2, 1]]
print(friend_requests_bfs(num_houses1, restrictions1, requests1)) 


num_houses2 = 5
restrictions2 = [[0, 1], [1, 2], [2, 3]]
requests2 = [[0, 4], [1, 2], [3, 1], [3, 4]]
print(friend_requests_bfs(num_houses2, restrictions2, requests2))  


