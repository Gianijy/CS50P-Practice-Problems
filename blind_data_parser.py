MESSY = ["10.5", "20", "hello", {"number": 5}, "30.1"]

def main():
    total = checkpoint()
    print(total)


def checkpoint():
    running_total = 0
    for something in MESSY:
        try:
            something_float = float(something)
        except (ValueError, TypeError):
            pass
        else:
            running_total += something_float
            continue
    
    return running_total

if __name__ == "__main__":
    main()