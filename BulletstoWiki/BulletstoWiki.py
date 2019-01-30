#! python3
# add * infront of each new line from clipboard

import pyperclip

#Pyperclip only str, int, float, and bool values can be copied to the clipboard, not list

text=pyperclip.paste()          #paste from clipboard

wiki=text.splitlines()          #split the line where there is \n -> this gives a LIST
for i in range(len(wiki)):
    wiki[i]='*'+ wiki[i]

text='.\n'.join(wiki)           #to copy modified text we need to join into string format for pyperclip
pyperclip.copy(text)



