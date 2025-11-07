stk = []
q = []

graph = {
    0 : [1,2,3],
    1 : [4,5,6], 
    2 : [7,8,9],
    3: [10,11,12],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
}

def format_string(val, pad):
    return ((pad * " ") + str(val))

def exists(collection: list[int], val: int):
    return_value = False
    if val in collection:
        return_value = True

    return return_value

def bfs(node, level):
    if node not in q:
        q.append(format_string(node, level))

    for child in graph[node]:
        q.append(format_string(child, level + 1))

    for child in graph[node]:
        if child not in q:
            bfs(child, level + 1)

def dfs(node, level):
    stk.append(format_string(node, level))
    children = graph[node]
    if len(children)> 0:
        for n in children:
            if not exists(stk, n):
                dfs(n, level + 1)

def main():
  dfs(0, 0)
  for i in stk:
    print(i)

  print("---------------------------------------")

  bfs(0, 0)
  for i in q:
    print(i)


if __name__ == "__main__":
    main()


      
