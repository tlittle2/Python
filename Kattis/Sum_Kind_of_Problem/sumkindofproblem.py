def main():
    d: dict[int, list[int]] = {}

    for _ in range(int(input())):
        a, b = map(int, input().split())

        d[a] = []
        d[a].append(sum(i for i in range (b+1)))
        d[a].append(b ** 2) #sum of first n odds
        d[a].append(b * (b + 1)) #sum of first n evens

    for k in d.keys():
        print(k, *d[k])


if __name__ == "__main__":
    main()
