def main():
    while True:
        x = int(input())
        if x == 0:
            break
        d = {}
        for i in range(x):
            case = list(input().split())
            for i in range(1, len(case)):
                if case[i] not in d.keys():
                    d[case[i]] = []
                d[case[i]].append(case[0])

        for j in d.values():
            j.sort()

        for k,v in sorted(d.items(), key=lambda x: x[0]):
            print(k, " ".join(i for i in v))

if __name__ == "__main__":
    main()
