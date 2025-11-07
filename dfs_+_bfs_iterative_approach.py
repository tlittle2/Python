mxN = 100

def reverseConnections(graph: dict[int, list[int]]):
    g = {}

    for key,value in graph.items():
        for v in value:
            g[v] = key
    return g

def has_cycles(g, root):
    r = reverseConnections(g)
    for k in r.keys():
        if r[k] != root and r[r[k]] == k: #if a key in a key/value pair exists as a value for some other key, and we aren't currently processing the root, we have a cycle
            return True
    return False

def graph_prechecks(g, root):
    assert 0 <= len(list(g.keys())) <= mxN, "Graph either has no data or is too big to traverse. Exiting"

    keys = set(g.keys())
    values = set(item for sublist in g.values() for item in sublist)
    assert values.difference(keys) != 0, "Invalid graph was potentially provided. Please investigate"

    assert not has_cycles(g, root), "Graph has cycles. Cannot perform dfs or bfs. Exiting"


def dfs_iterative_traversal(graph, root) -> list[int]:
    graph_prechecks(graph, root)

    stk = []
    vis = {i : False for i in graph.keys()}
    return_value = []
    
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
    graph_prechecks(graph, root)

    mstr_q = []

    mstr_q.append(root)

    for _ in range(mxN):
        if len(mstr_q) == len(list(graph.keys())) -1:
            return mstr_q
        for node in mstr_q:
            for n in graph[node]:
                mstr_q.append(n)
    
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
