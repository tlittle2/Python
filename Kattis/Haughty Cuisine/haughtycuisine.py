def main():
    myList = []

    menus = int(input())
    for i in range(menus):
        myList = input().split(" ")

    
    for i in myList:
        print(i)
        

if __name__ == "__main__":
    main()
