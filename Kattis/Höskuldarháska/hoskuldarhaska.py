import functools

def main():
    n = int(input())

    d = {}
    for i in range(n):
        line = input().split()
        data = line[1:]
        d[i] = data

    for i in d.values():
        i.sort()

    p = functools.reduce(lambda acc, x: [(i + (j,)) for i in acc for j in x],d.values() , [()])

    for i in p:
        print(" ".join(i))

if __name__ == "__main__":
    main()
