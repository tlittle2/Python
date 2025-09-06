from math import floor
def main():
    scale ={
        range(90,100): 'A',
        range(80,90) : 'B',
        range(70,80) : 'C',
        range(60,70) : 'D',
        range(0,60)  : 'F',
    }

    grades = list(map(int, input().split(maxsplit=3)))
    weights = [0.25, 0.25, 0.50]

    avg = floor(sum(grade * weight for grade,weight in zip(grades, weights)))
 
    print("".join(v for k,v in scale.items() if avg in k))

if __name__ == "__main__":
    main()
