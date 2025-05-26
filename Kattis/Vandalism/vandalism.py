def main():
    lst = ['U','A','P','C']
    
    diffs = set(lst).difference(set(input()))

    for i in lst:
        if i in diffs:
            print(i, sep = "", end = "")
    
if __name__ == "__main__":
    main()
