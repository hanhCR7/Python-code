print("CCHATBOT: HELLO, WHAT`S YOUR NAME?")
name = input("YOU: ")
print(f"Chatbot: Hello {name}")
print("Chatbot: WHAT INFORMATION DO YOU WANT TO KNOW ?")
answer = input(f"{name}: ")
if answer == "how are you":
    print("Chatbot: I'm just a computer program, but I'm here and ready to help!")
if answer == "goodbye":
    print("Chatbot: Goodbye! Have a great day!")