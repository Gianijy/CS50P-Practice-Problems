import sys
from statistics import mean, median, mode


def main():
    final = command_validator()
    print(f"{final:.4f}")
    
    
def command_validator():
    while True:
        try:
            operation = sys.argv[1].lower()
            if operation not in ["mean", "median", "mode"]:
                sys.exit("Invalid operation.")
            
            values = [float(value) for value in sys.argv[2:]]
        except IndexError:
            sys.exit("Too few arguments.")
        except ValueError:
            sys.exit("Values must be numbers.")
        else:
            match operation:
                case "mean":
                    return mean(values)
                case "median":
                    return median(values)
                case "mode":
                    return mode(values)
            

if __name__ == "__main__":
    main()