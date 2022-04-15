import requests


api_endpoint = "https://api.funtranslations.com/translate/morse"

text_input = input("Please enter the text you wish to convert to morse code\n")

parameters = {
    "text": text_input
}

response = requests.post(url=api_endpoint, json=parameters)

morse_code = response.json()["contents"]["translated"]

formatted_morse_code = morse_code.replace("   ", "/")

print(f"Original Text: {text_input}")
print(f"Morse Code: {formatted_morse_code}")
