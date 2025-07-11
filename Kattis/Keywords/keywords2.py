def main():
    print(len(set([input().upper().replace("-", " ") for _ in range(int(input()))])))

if __name__ == "__main__":
    main()
