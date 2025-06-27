def getSum():
    return sum([i for i in map(int, input().split())])

def main():
    input().split()
    
    a = getSum()
    b = getSum()

    if a==b:
        print("Oh no")
    else:
        print("Button 1" if a > b else "Button 2")

if __name__ == "__main__":
    main()
