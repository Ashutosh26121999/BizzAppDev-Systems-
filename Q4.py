'''
4. Provide a program to read the file from URL and display the content
in terminal.
• The file URL has to be input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.
'''
import urllib.request

url = input("URL file path:")
file = urllib.request.urlopen(url)

for line in file:
    decoded_line = line.decode("utf-8")
    print(decoded_line)
