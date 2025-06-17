
filename = "output.txt"

#ASSUMING THAT WE ARE CREATING A NEW FILE AND FILE DOES NOT EXIST

datatowrite = input("Enter text to write to the file: ")

with open(filename, 'w') as myfilewrite:
    myfilewrite.write(datatowrite)
    print("Data Successfully written to output.txt")

#NOW APPENDING TO THE FILE AS PREVIOUS CODE HAS CREATED THE FILE

datatoappend = input("Enter additional text to append: ")

with open(filename, 'a') as myfileappend:
    myfileappend.write("\n" + datatoappend)
    print("Data successfully appended")

#PRINTING THE ENTIRE FILE TO CONSOLE

with open(filename, 'r') as myfileread:
    print("Final content of", filename,":")
    while(line := myfileread.readline()):
        print(line.strip())
