import heapq

# heapq를 활용하여 구현
# n,m = map(int, input().split()) # n = 노드개수, m = 간선 개수
# k = int(input()) # 시작노드
n, m = 5,6
k = 1
INF = 1e8 # inf를 큰 수로 설정

# graph = [[] for _ in range(n+1)] # 그래프에 대한 정보를 담는 list
graph = [[], [(2, 1), (3, 3)], [(3, 1), (4, 5)], [(4, 2)], [], [(1, 1)]]
visited = [False] * (n+1) # 방문했는지의 여부를 확인하는 list
distance = [INF] * (n+1) # 최단 거리 테이블

# 그래프에 대한 정보를 입력
# for _ in range(m):
#     u,v,w = map(int, input().split()) # u = 출발노드, v = 도착노드, w = 연결된 간선의 가중치
#     graph[u].append((v,w)) # 출발노드는 index를 통해서 매칭하고 v,w를 입력

    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(dist+ i[1],i[0]))
dijkstra(k)
print(distance)