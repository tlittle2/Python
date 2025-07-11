from datetime import datetime

def main():
    s = input().split(" ")

    s[2] = s[2].removeprefix("/")

    year = "20{}".format(s[3])
    month = "{:02}".format(datetime.strptime(s[2], "%b").month)
    day = s[0]

    print("{}-{}-{}".format(year, month, day))

if __name__ == "__main__":
    main()
