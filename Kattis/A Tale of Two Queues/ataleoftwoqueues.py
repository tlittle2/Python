def main():
    map(int, input().split())

    ls = sum(list(map(int, input().split())))
    rs = sum(list(map(int, input().split())))

    if ls < rs:
        print("left")
    elif ls > rs:
        print("right")
    else:
        print("either")

if __name__ == "__main__":
    main()
