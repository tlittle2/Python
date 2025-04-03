def main():
    ip= list(map(str, input().strip()))
    newIp= [ip[i] for i in range(0, len(ip), 3)]

    #Answer: max occurrence of a character from the input
    print(max({newIp[i]: newIp.count(newIp[i]) for i in range(len(newIp))}.values()))

if __name__ == "__main__":
    main()
