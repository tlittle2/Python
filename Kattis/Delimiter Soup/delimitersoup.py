def main():
    d = {
        "]":"[",
        "}":"{",
        ")":"("
    }

    stk = []
    badMatch = ""

    int(input())
    ip = input()

    for i in range(len(ip)):
        if ip[i] in d.values(): #if current char is an opening delimiter, push it to the stack
            stk.append(ip[i])
        
        elif ip[i] in d.keys(): #if current char is a closing delimiter
            if stk and d[ip[i]] == stk[-1]: # and it's matching opening delimiter is currently at the top of the stack
                stk.pop() #pop opening delimiter off the stack
            else:
                badMatch = "{} {}".format(ip[i], i) #otherwise, add this match.
                break #Only want first occurrence, so break from here
    
    print(badMatch if badMatch else "ok so far")
                        
if __name__ == "__main__":
    main()
