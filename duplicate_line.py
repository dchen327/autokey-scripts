'''
Duplicate the current line beneath it (similar to sublime ctrl+shift+d)
'''
keyboard.send_keys('<end>')
keyboard.send_keys('<shift>+<home>')
keyboard.send_keys('<ctrl>+c')
keyboard.send_keys('<end>')
keyboard.send_keys('<enter>')
keyboard.send_keys('<ctrl>+v')
