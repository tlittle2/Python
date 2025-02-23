def main():
    first = {}
    second = {}
    
    n = int(input())

    #append inputs to respective dictionaries
    for _ in range(n):
        ans = input()
        if ans not in first.keys():
            first[ans] = 1
        else:
            first[ans]+= 1

    for _ in range(n):
        ans = input()
        if ans not in second.keys():
            second[ans] = 1
        else:
            second[ans]+= 1

    
    #make sure both dictionaries have the same keys (to normalize comparison)
    for k in second.keys():
        if k not in first.keys():
            first[k] = 0

    for k in first.keys():
        if k not in second.keys():
            second[k] = 0

    #the answer is the sum of the minimum value for each key from both of dictionaries (both dictionaries have the same keys, so the dictionary we choose to iterate through does not matter)
    print(sum(min(first[k], second[k]) for k in first.keys()))


if __name__ == "__main__":
    main()
