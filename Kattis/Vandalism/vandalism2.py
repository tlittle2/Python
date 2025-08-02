def main():
    lst = ['U','A','P','C']
    
    diffs = set(lst).difference(set(input()))

    print("".join((i for i in lst if i in diffs)))

if __name__ == "__main__":
    main()
