#!/usr/bin/env python3

import sys, string

morseDict= {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': "-.-",
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p':'.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',

    ' ': '   ',

    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....--',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '10': '-----',

    '.': '  '
}


def wordToMorse():
    morse= ""
    print("Please enter a word: ")
    word = str(sys.stdin.readline().rstrip())
    
    for i in word.lower():
        for key, value in morseDict.items():
            if i == key:
                morse+=value + " "
    return morse
    
  

def morseToEnglish():
    print("Please enter your morse sequence:")
    sequence = sys.stdin.readline().rstrip().split('  ')

    for word in sequence:
        for letter in word.split():
            for key, value in morseDict.items():
                if letter == value:
                    print(key, end= '')
        print()


def main():
    print("Do you want to convert word/sentence to morse(1), or morse to word/sentence(2)?")
    answer = int(sys.stdin.readline())
    if answer == 1:
        encrypted = wordToMorse()
        print(encrypted)
        
    else:
        morseToEnglish()


if __name__ == "__main__":
    main()

