FILENAME = "my_notes.txt"

# -- Open the file for reading
f = open(FILENAME, 'r')

# -- Read the content of the file
contents = f.read()

# -- Print the contents
print("File: ", f.name)
print(contents)

# -- Closing the file
f.close()

# -- Open again for adding
f = open(FILENAME, "a")

# -- write some information to the file
f.write("Helllo!!!! just writing into your file!\n")

f.close()

print("End")