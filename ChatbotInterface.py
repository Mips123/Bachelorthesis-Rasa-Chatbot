import requests
import json

# localhost address
rasa_server_url = "http://localhost:5005/webhooks/rest/webhook"

# list for savin conversation
conversation = []


def send_message(message):
    data = {"sender": "user", "message": message}
    try:
        response = requests.post(rasa_server_url, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failure while sending the request to Bot-Server:", e)
        return []


def run_chatbot():
    while True:
        user_input = input("User: ")

        if user_input.lower() == "stop":
            break

        response = send_message(user_input)

        conversation.append({"user": user_input, "Bot": response})

        if not response:
            print("The chatbot does not answer")
        if response:
            if response.__len__() == 0:
                print("Bot did receive request but did not answer")
            else:
                for message in response:
                    print("BobTheBot: " + message['text'])

    print()

    # Savin conversation
    with open("conversation.json", "w") as json_file:
        json.dump(conversation, json_file)


if __name__ == '__main__':
    run_chatbot()
