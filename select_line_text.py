'''
Select the text in the current line, but don't select the entire line.
This doesn't select surrounding spaces.
'''
keyboard.send_keys('<end>')
keyboard.send_keys('<shift>+<home>')