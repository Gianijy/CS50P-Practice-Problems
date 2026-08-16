DICT = {
    "web" : "JavaScript",
    "games" : "C#",
    "data" : "Python",
    "mobile" : "kotin",
    "systems" : "C"
}


def main():
    category = get_input()
    recommended = recommend(category)
    print(f"If you want to build in the {category} category, the recommended language to learn is {recommended}")


def get_input():
    print("Choices:\nWeb\nGames\nData\nMobie\nSystems")
    category = input("What do you want to build: ").lower()
    return category


def recommend(category):
    for cate, language in DICT.items():
        if cate == category:
            return language


if __name__ == "__main__":
    main()