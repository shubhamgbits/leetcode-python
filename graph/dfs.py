from graphExamples import example1
graph = example1

def dfs(source):
    print(source)
    for neighbour in graph[source]:
        dfs(neighbour)

def dfs2(source):
    print(source)
    [dfs(neighbour) for neighbour in graph[source]]

def dfs_with_stack(stack):
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


dfs_with_stack(['a'])
# dfs('a')
# print("\n")
# dfs2('a')
