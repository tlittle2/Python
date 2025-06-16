def main():
    d = {}

    for i in range(int(input())):
        name = input()
        for idx, char in enumerate(name):
            if char.isupper():
                d[name[idx:len(name)]] = name
                break

    for i in sorted(d):
        print(d[i])

if __name__ == "__main__":
    main()
