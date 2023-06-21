#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_txt = letter.read()
    #print(letter_txt)
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.read()
    listed = name_list.split()
    #print(listed)
for name in listed:
    named_letter = letter_txt.replace("[name]", name)
    filename = f"letter_for_{name}.txt"
    with open(f"./Output/ReadyToSend/{filename}", mode="x" ) as output:
        filename = output.write(named_letter)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp