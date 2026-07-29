import requests
import json

def main():
    ninja()


def ninja():
    response = requests.get("https://catfact.ninja/fact")

    data = response.json()
    formatted_data = json.dumps(data, indent=4)

    print(formatted_data)
    print(data["fact"])


if __name__ == "__main__":
    main()

