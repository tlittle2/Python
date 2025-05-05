def main():
    int(input())
    ip = input().split()

    d = {}

    for _ in range(int(input())):
        t = input().split()
        d[t[0]] = t[1]
    
    print(" ".join(d[i] for i in ip))

if __name__ == "__main__":
    main()
