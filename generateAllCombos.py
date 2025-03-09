import itertools
def main():
    #numbers = [1, 2, 3, 4, 5]
    addressLines = ['3416', 'Highview', 'Road', 'Suite', '1000']
    for r in range(1, len(addressLines) + 1):
        for combination in itertools.combinations(addressLines, r):
            result = [str(num) if num in combination else "" for num in addressLines]
            print(",".join(result))


if __name__ == "__main__":
    main()
