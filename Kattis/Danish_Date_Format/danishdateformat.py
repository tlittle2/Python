def main():
    d = {
    1 : "januar",
    2 : "februar",
    3 : "marts",
    4 : "april",
    5 : "maj",
    6 : "juni",
    7 : "juli",
    8 : "august",
    9 : "september",
    10 : "oktober",
    11 : "november",
    12 : "december"
    }

    ip = list(map(int, input().split("/")))

    print("{}. {} {}".format(ip[1], d[ip[0]], ip[2]))


if __name__ == "__main__":
    main()
