def main():
    l,h = map(int, input().split())

    d = {i : "" for i in range(h)}

    board = [[i for i in input()] for _ in range(l)]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                d[j] = board[i][j]

    for i in range(h):
        print(d[i], end="")

if __name__ == "__main__":
    main()
