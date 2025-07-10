def main():
    seats, _ = map(int, input().split())

    g = [int(i) for i in input().split()]

    idx = s = 0

    for i in range(len(g)):
        if s+g[i] > seats:
            idx = i
            break
        else:
            s+=g[i]
    
    print(len(g) - idx)

if __name__ == "__main__":
    main()
