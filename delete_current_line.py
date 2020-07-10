'''
Delete entire current line
'''
keyboard.send_keys('<end>')
keyboard.send_keys('<shift>+<home>')
keyboard.send_keys('<delete>')