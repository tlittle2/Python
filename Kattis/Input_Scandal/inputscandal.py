from sys import stdin
def main():
    lst = []

    for line in stdin:
        lst.append(line)

    print(len(lst))
    for i in lst:
        print(i)
        
if __name__ == "__main__":
    main()
