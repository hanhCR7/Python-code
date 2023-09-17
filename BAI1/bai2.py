
print("CHATBOT: HELLO, WHAT`S YOUR NAME?")
name = input("YOU: ")
print(f"Chatbot: Hello {name}")
print("Chatbot: WHAT INFORMATION DO YOU WANT TO KNOW ?")
answer = input(f"{name}: ")
if answer == "how are you":
    print("Chatbot: I'm just a computer program, but I'm here and ready to help!")
elif answer == "IT":
    print("Chatbot: Information Technology (IT) refers to the use of computers,"
          " software, networks, and other technologies to manage and process information."
          " It encompasses a wide range of activities related to computing and technology, "
          "including the development, management, and maintenance of computer systems, "
          "software applications, and networks.")
elif answer == "goodbye":
        print("Chatbot: Goodbye! Have a great day!")
else:
    print("Chatbot: I'm sorry, I didn't quite understand that.")