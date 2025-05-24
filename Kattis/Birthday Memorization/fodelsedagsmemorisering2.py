from collections import defaultdict
def main():
    likes = {}
    birthdays = defaultdict(list)
    
    for i in range(int(input())):
        name, like, birthday = input().split()
     
        birthdays[birthday].append(name) #birthday dict will group everyone who has the same birthday.
        likes[name] = int(like) #likes will just be a dict of a person's likeness score

        
    ans = []
    for v in birthdays.values(): #for each list entry in birthdays (birthday : [list of people])
        
        joinDict = {likes[i]: i for i in v} #"join" on birthday and likes on the basis of person

        ans.append(joinDict[max(joinDict.keys())])# get max "like" for each group (guaranteed to be distinct according to problem)

    print(len(ans))
    for i in sorted(ans):
        print(i)

if __name__ == "__main__":
    main()
