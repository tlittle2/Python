def main():
    d = {}

    for i in range(int(input())):
        ip = input().split()
        apps = ip[1:len(ip)]
        for j in apps:
            if j in d:
                d[j] = min(d[j], i)
            else:
                d[j] = i
                break
    
    for k in d.keys():
        print(k, sep = " ", end = " ")


if __name__ == "__main__":
    main()
