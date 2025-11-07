mxN = 100

def reverseConnections(graph: dict[int, list[int]]):
    g = {}

    for key,value in graph.items():
        for v in value:
            if v not in g.keys():
                g[v] = [key]
            else:
                g[v].append(key)
    return g

def graph_prechecks(g):
    assert 0 <= len(list(g.keys())) <= mxN, "Graph either has no data or is too big to traverse. Exiting"

    keys = set(g.keys())
    values = set(item for sublist in g.values() for item in sublist)
    assert values.difference(keys) != 0, "Invalid graph was potentially provided. Please investigate"

def create_visited_map(g: dict[int, list[int]]):
    return {i : False for i in g.keys()}


def dfs_iterative_traversal(graph, root) -> list[int]:
    graph_prechecks(graph)
    vis = create_visited_map(graph)

    return_value = []

    stk = []
    stk.append(root)

    for _ in range(mxN):
        if len(stk) == 0:
            return return_value
        top = stk.pop()
        #print("top: {}".format(top))
        if not vis[top]:
            vis[top] = True
            return_value.append(top)
            for i in graph[top]:
                stk.append(i)
                #print(stk)
        #print(vis)

def bfs_iterative(graph, root) -> list[int]:
    graph_prechecks(graph)
    vis = create_visited_map(graph)

    mstr_q = []
    mstr_q.append(root)

    for _ in range(mxN):
        if len(mstr_q) == len(graph.keys()):
            return mstr_q
        for node in mstr_q:
            for n in graph[node]:
                if not vis[n]:
                    mstr_q.append(n)
                    vis[n] = True

    
def main():
    g = {
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
    

    print(dfs_iterative_traversal(g,0))
    print(bfs_iterative(g, 0))
    print(reverseConnections(g))

if __name__ == "__main__":
    main()
