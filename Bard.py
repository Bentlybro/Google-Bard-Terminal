import bardapi
import os

os.environ['_BARD_API_KEY'] = "__Secure-1PSID-Key-Here"
  
while True:
    input_text = []
    print("Type A Message And Use !fin Once Finished, or type 'exit' to exit")
    while True:
        user_input = input("")
        if user_input == "!fin":
            break
        if user_input == "exit":
            exit()
        input_text.append(user_input)

    input_text = "\n".join(input_text).replace("!fin", "")

    response = bardapi.core.Bard().get_answer(input_text)

    output_text = response['content']
    print("Google Bard API reply:", output_text)