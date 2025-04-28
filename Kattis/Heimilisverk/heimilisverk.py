def main():
    ip = int(input())
    d = dict()

    for _ in range(ip):
        i = input()
        d[i] = 0

    for i in d.keys():
        print(i)

if __name__ == "__main__":
    main()
