blacklisted_word = "shit"
statement = input("Send message: ")
if(blacklisted_word in statement):
    print("You have been muted for: using a blacklisted word")
else:
    print(statement)