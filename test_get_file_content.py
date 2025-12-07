from functions.get_file_content import get_file_content

separator = 50*"="

print("Test: main.py")
print(get_file_content("calculator", "main.py"))
print(separator)
print("Test: pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))
print(separator)
print("Test: /bin/cat")
print(get_file_content("calculator", "/bin/cat"))
print(separator)
print("Test: file_not_exist")
print(get_file_content("calculator", "does_not_exist.py"))

