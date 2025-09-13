import math
def main():
    opposite, angleInDegree = map(int, input().split())

    adjacent = opposite / math.tan(math.radians(angleInDegree))
    hypotenuse = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))

    print(math.ceil(hypotenuse))
 
if __name__ == "__main__":
    main()
