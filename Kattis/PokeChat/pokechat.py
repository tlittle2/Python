def main():
    string = input()
    encodedString = input()
    windowIdx = 3

     #new index revealed every 3 byte sliding window
    encodedList = [int(encodedString[i:i+windowIdx]) for i in range(0, len(encodedString), windowIdx)]

    ans = ""
    for i in range(len(encodedList)):
        ans += string[encodedList[i]-1]

    print(ans)

if __name__ == "__main__":
    main()
