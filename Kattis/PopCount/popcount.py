def main():
    s = input()

    print(sum(1 if s[i] == '1' else 0 for i in range(len(s))))

if __name__ == "__main__":
    main()
