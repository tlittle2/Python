def main():
    s = input()

    d = {i : s.count(i) for i in s}
    repeatChar = 'e'
    
    print("{}{}{}".format(s[0], repeatChar * (d[repeatChar] * 2) ,s[len(s) -1]))

if __name__ == "__main__":
    main()
