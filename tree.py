# Write your code here :-)
import os

path = os.path.abspath('/Users/nikki/documents/labs/python/pypart8')
file1 = open("NewFile.txt", "w")

file1.write("Hello, I am writing some words.")
file1.close()

