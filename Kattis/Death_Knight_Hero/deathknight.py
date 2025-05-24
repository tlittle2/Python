def main():
    ans = 0
    
    for _ in range(int(input())):
        if input().find('CD') == -1:
            ans +=1

    print(ans)

if __name__ == "__main__":
    main()
