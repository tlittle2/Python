from collections import defaultdict
def main():
    likes = {}
    birthdays = defaultdict(list)

    #birthday dict will group everyone who has the same birthday. likes dict will just contain a person's likeness score
    for i in range(int(input())):
        name, like, birthday = input().split()
     
        birthdays[birthday].append(name)
        likes[name] = int(like)

        
    ans = []
    for v in birthdays.values(): #for each "birthday" (which will have 1 or more people associated)
        tempDict = {}
        for i in v:
            tempDict[likes[i]] = i # "join" on birthdays and likes dictionaries on the basis of person
        
        ans.append(tempDict[max(tempDict.keys())])# get max like for each group (guaranteed to be distinct according to problem)

    print(len(ans))
    for i in sorted(ans):
        print(i)

if __name__ == "__main__":
    main()
