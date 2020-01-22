print('''Hello, Welcome to a basic version of the popular Hangman game.
There is a limit of 5 wrong attempts.
Enter one letter at a time.
''')
word = "python"
blanks = "_" * len(word)
blanksplit = []
for j in blanks:
    blanksplit.append(j)
# print(blanksplit)


got = False
count = 0

wordsplit = []
for i in word:
    wordsplit.append(i)
# print(wordsplit)



while got == False:
    user_input = input("Take a guess here:").lower()

    if user_input in wordsplit:
        # print("yaay")
        h = word.find(user_input)
        blanksplit.pop(h)
        blanksplit.insert(h, user_input)
        final = ""
        for h in blanksplit:
            final += h
        print(final)
        if final == word:
            got = True
        pass

    elif user_input not in wordsplit:
        count += 1
        print("You have", 5- count, "tries left")
        pass

    if count == 5:
        print("Oops... You failed")
        break


if got == True:
    print('''Congrats! You won!!!
    Thanks for playing
    -Ankit''')
input('Press ENTER to exit') 