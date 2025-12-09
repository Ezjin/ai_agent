from functions.run_python_file import run_python_file

separator = 50*"="+"\n"

print("Test: main.py without args")
print(run_python_file("calculator", "main.py"))
print(separator)

print("Test: main.py with args")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(separator)

print("Test: calculator tests.py")
print(run_python_file("calculator", "tests.py"))
print(separator)

print("Test: ../main.py")
print(run_python_file("calculator", "../main.py"))
print(separator)

print("Test: non existend file")
print(run_python_file("calculator", "nonexistent.py"))
print(separator)

print("Test: lorem.txt")
print(run_python_file("calculator", "lorem.txt"))
