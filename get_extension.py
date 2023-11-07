#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java
#Output : java

input = input("Enter a filename: ")

f_exten = input.split(".")
print("The extension of the file is: " + repr(f_exten[-1]))