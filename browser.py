import webbrowser, sys

sys.argv

#Check if cmd line args were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open()
    
