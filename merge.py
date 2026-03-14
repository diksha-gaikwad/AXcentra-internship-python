file1 = "file1.txt"
file2 = "file2.txt"
merged_file = "merged.txt"

# Create files if they don't exist
open(file1, "a").close()
open(file2, "a").close()

with open(file1, "r") as f1:
    data1 = f1.read()

with open(file2, "r") as f2:
    data2 = f2.read()

with open(merged_file, "w") as f:
    f.write(data1 + "\n" + data2)

print("Files merged successfully.")
