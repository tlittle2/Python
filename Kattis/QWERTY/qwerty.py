def main():
    d = {
    "a"	: "q",
    "b"	: "w",
    "c"	: "e",
    "d"	: "r",
    "e"	: "t",
    "f"	: "y",
    "g"	: "u",
    "h"	: "i",
    "i"	: "o",
    "j"	: "p",
    "k"	: "a",
    "l"	: "s",
    "m"	: "d",
    "n"	: "f",
    "o"	: "g",
    "p"	: "h",
    "q"	: "j",
    "r"	: "k",
    "s"	: "l",
    "t"	: "z",
    "u"	: "x",
    "v"	: "c",
    "w"	: "v",
    "x"	: "b",
    "y"	: "n",
    "z"	: "m",
    " " : " " 
    }

    int(input())
    for i in input():
        print(d[i], sep = "", end = "")

if __name__ == "__main__":
    main()
