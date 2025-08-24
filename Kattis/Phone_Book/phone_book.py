def main():
    n = 0
    for _ in range(int(input())):
        phone = input()
        prefixLength = 3
        country_code = phone[0:prefixLength]
        digits = phone[prefixLength: len(phone)]

        if country_code == "+39" and len(digits) in [9,10]:
            n += 1
    
    print(n)

if __name__ == "__main__":
    main()
