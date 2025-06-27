def main():
    input().split()

    def getSum(ip):
        return sum([i for i in map(int, ip)])

    a = getSum(input().split())
    b = getSum(input().split())

    if a==b:
        print("Oh no")
    else:
        print("Button 1" if a > b else "Button 2")

if __name__ == "__main__":
    main()
