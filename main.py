blacklisted_words = ["shit", "ass", "fuck"]
statement = input("Send message: ")
for blacklisted_word in blacklisted_words:
    if(blacklisted_word in statement):
        print("you have been muted for saying a blacklisted word")