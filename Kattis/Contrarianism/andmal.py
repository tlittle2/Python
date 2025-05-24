import random
from string import ascii_letters

def main():
    input()
    print(''.join(random.choice(ascii_letters) for _ in range(10)))    

if __name__ == "__main__":
    main()
