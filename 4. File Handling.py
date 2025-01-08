# File
file_name = "sample.txt"

# Write to the file
with open(file_name, "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Read and display
with open(file_name, "r") as file:
    content = file.read()
    print("File contents:\n", content)
