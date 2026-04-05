def main():
    ip = input()
    f = "tree"
    o = ip.find(f)

    print(o if o != -1 else "no trees here")

if __name__ == "__main__":
    main()
