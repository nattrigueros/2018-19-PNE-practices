# Example of reading a file located
# in our local filesystem

# -- Filename to read
NAME = "my_notes.txt"

# -- Open the file
myfile = open(NAME, 'r')

# -- myfile is an object!!! Let's see what it has inside

# -- Print the filename
print("Print: file opened:", myfile.name)

# -- Read the whole file into a string
contents = myfile.read()

# -- Print the files's contents
print("The file contents are:", contents)
print("The end!")

# -- Close the file
myfile.close()
