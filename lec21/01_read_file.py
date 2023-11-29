f = open("lec21/01_read_file.py", "r")
lines = f.read()

print(f"File object: {f}")

print("The contents of the file are: ")
print(lines.upper())

lines = f.read() # try to read again
print("The lines the second time are: ")
print(lines.upper())

f.close()