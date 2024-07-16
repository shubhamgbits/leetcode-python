from graphExamples import example1
graph = example1

queue = []

def bfs(start):
    queue.append(start)
    while len(queue) > 0:
        source = queue.pop(0)
        print(source)
        for neighbour in graph[source]:
            queue.append(neighbour)


bfs('a')
