def main():
    ranges: list[int] = list(map(int, input().split()))
    grade: int = int(input())
    d: dict[str, list] = {}

    mx: int = 101
    curr: str = 'A'
    for i in ranges:
        d[curr] = [i, mx]
        mx = i - 1
        curr = chr(ord(curr) + 1)

    d[chr(ord(curr))] = [-1, mx]
    print(' '.join(k for k,v in d.items() if grade >= v[0] and grade <= v[1]))

if __name__ == "__main__":
    main()
