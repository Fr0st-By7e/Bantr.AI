from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

companion_roles = [os.getenv("Sharma-ji-ka-Beta"), os.getenv("Cinema-Rasigan"), os.getenv("Sporty-Chettan")]

genai.api_key = os.getenv("Gemeni_API")
client = genai.Client(api_key=genai.api_key)

'''contents = input("User: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=contents
)

print("AI: " + response.text)'''

companions = {
    "Sharma-ji ka Beta": os.getenv("Sharma-ji-ka-Beta"),
    "Cinema Rasigan": os.getenv("Cinema-Rasigan"),
    "Sporty Chettan": os.getenv("Sporty-Chettan")
}

def chat_with_companion(companion_type, message):
    prompt = companions[companion_type] + "\nUser: " + message

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text

def chat_Cinema_Rasigan(message):
    return chat_with_companion("Cinema Rasigan", message)

def chat_Sharma_ji_ka_Beta(message):
    return chat_with_companion("Sharma-ji ka Beta", message)

def chat_Sporty_Chettan(message):
    return chat_with_companion("Sporty Chettan", message)

if __name__ == "__main__":
    api_running = True
    while api_running:
        companion_type = input("Select a companion: ")
        message = input("User: ")
        response = chat_with_companion(companion_type, message)
        print("AI: " + response)
        continue_chat = input("Do you want to continue chatting? (yes/no): ")
        if continue_chat.lower() != "yes":
            api_running = False