import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client =genai.Client(api_key= os.environ["GEMINI_API_KEY"])

chat = client.chats.create(
    model = "gemini-3.5-flash",
    config = genai.types.GenerateContentConfig(
        system_instruction ="You are a friendly encouraging coding tutor who explains things simply"
    )
)
while True:
    user_input = input("You: ")

    if user_input =="quit":
        break
    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("something went wrong", e)
        print("Let's try again, go ahead and type your message.")