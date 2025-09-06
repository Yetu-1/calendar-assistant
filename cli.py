import requests

API_URL = "http://127.0.0.1:8000/assistant"

def main():
    print("🤖 Calendar Assistant (type 'exit' to quit)")
    while True:
        query = input("> ")
        if query.lower() == 'exit':
            break
        resp = requests.post(API_URL, json={"query" : query})
        if resp.status_code == 200:
            print("Assistant: ", resp.json()["response"])
        else: 
            print("Error", resp.text)

if __name__ == "__main__":
    main()