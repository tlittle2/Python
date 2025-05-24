def main():
    filename = input().split('.')

    print(".{}".format(filename[len(filename)-1]))

if __name__ == "__main__":
    main()
