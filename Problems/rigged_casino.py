import random

def main():
    redp, blackp, greenp = roulette()
    print(f"Red was picked: {redp} times")
    print(f"Black was picked: {blackp} times")
    print(f"Green was picked: {greenp} times")


def roulette():
    colors = ["Red", "Black", "Green"]
    pick = random.choices(colors, weights = [49, 49, 2], k = 10000)
    red = 0 
    black = 0 
    green = 0
    
    for color in pick:
        if color == "Red":
            red += 1
        elif color == "Black":
            black += 1
        elif color == "Green":
            green += 1
            
    return red, black, green

if __name__ == "__main__":
    main()