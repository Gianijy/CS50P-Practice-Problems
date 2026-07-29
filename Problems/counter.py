def main():
    sentence = input("Please enter a sentence: ")
    letters, digits, spaces, others = counter(sentence)
    print(f"Letters: {letters}\nDigits: {digits}\nSpaces: {spaces}\nOther: {others}")

def counter(sentence):
    letters = 0
    digits = 0
    spaces = 0
    others = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1

    return letters, digits, spaces, others


if __name__ == "__main__":
    main()
