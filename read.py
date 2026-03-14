filename = "sample.txt"

# Create file if not exists
with open(filename, "a"):
    pass

# Read file
with open(filename, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
