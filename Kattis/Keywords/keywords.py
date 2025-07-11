def main():
    s = set()
    for _ in range(int(input())):
        s.add(input().upper().replace("-", " "))

    print(len(s))

if __name__ == "__main__":
    main()
