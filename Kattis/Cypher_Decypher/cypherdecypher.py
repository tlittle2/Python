def main():
    mult = [int(i) for i in list(input())]

    l = ord('A')
    u = ord('Z') + 1

    mp = {chr(i) :i-l for i in range(l,u)}
    mp2 = {i-l :chr(i) for i in range(l,u)}

    for _ in range(int(input())):
        wrd = list(input())
        newword = str()
        for w in range(len(wrd)):
            idx = (mp[wrd[w]]  * mult[w]) % (u-l)
            newword += mp2[idx]
        print(newword)
        
if __name__ == "__main__":
    main()
