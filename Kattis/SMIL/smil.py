def main():
    figures = [
          [":", ")"]
        , [";", ")"]
        , [":","-",")"]
        , [";","-",")"] 
        ]

    s = list(input())
    
    for i in range(len(s)):
        nose = list(s[i:i+3])
        noNose = list(s[i:i+2])
        if nose in figures or noNose in figures:
            print(i)
 
if __name__ == "__main__":
    main()
