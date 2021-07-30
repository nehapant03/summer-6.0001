
word = "ab"
myLetters = "abcd"
for letter in word:
    index = myLetters.find(letter)
    print("found ", letter)
    if index != -1:
        myLetters = myLetters[0:index] + myLetters[index + 1::]
print(myLetters)