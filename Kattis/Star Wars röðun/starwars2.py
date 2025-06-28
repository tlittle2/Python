def main():
    l = int(input())
    eq = l // 3

    #sort the list, and create dictionary out idx of character and the character itself
    d = {idx : i for idx, i in enumerate(sorted(list(map(int, input().split()))))} 

    ans = []

    for i in range(eq,eq*2): #take care of the middle indices first, and remove them from the dictionary once done to maintain sorted order
        ans.append(d[i])
        d.pop(i)

    for i in d.values(): #append the rest
        ans.append(i)

    for i in ans:
        print(i, sep = " ", end = " ")

if __name__ == "__main__":
    main()
