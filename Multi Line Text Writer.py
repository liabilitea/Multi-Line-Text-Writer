#Write a new txt file and assign it as a variable
with open("mylife.txt", "w") as output_file:

    #Use loop to continuously ask the user to input info in new lines
    while True:
        #Ask user to input any text to be written into the file
        new_line = input("Please enter any information about you in this line: ")
        #Write the input text into the file and append a new line character at the end
        output_file.write(new_line + "\n")
        #Ask user if they want to write more information

#Exit loop
