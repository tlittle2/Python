def main():
    n= o = 0

    for _ in range(int(input())):
        ip = input().split()
        v = int(ip[2])
        if ip[1] == 'IN':
            n += v
        else:
            o += v

    print("NO STRAGGLERS" if n == o else abs(n - o))
    

if __name__ == "__main__":
    main()
