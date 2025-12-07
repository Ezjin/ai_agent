from functions.write_file import write_file

separator = 50*"="

print("Test: write lorem.txt")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(separator)
print("Test: pgk/morelorem.txt")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(separator)
print("Test: tmp/temp.txt")
print(write_file("calculator", "/temp/temp.txt", "this should not be allowed"))
