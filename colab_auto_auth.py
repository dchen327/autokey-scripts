'''
Automatically authenticate GDrive in GColab to first user in account list
Change number of tabs after "select right email" to select different accounts.
'''
from time import sleep
# run cell
keyboard.send_keys('<ctrl>+<enter>')
sleep(1.5)
keyboard.send_keys('<shift>+<tab>')
# launch authorization page
keyboard.send_key('<enter>')
sleep(1.5)
# select right email
keyboard.send_key('<tab>', repeat=3)
keyboard.send_key('<enter>')
sleep(2)
# move to allow button
keyboard.send_key('<tab>', repeat=11)
keyboard.send_key('<enter>')
sleep(2)
# copy auth code
keyboard.send_key('<tab>', repeat=2)
keyboard.send_key('<enter>')
keyboard.send_keys('<ctrl>+w')
sleep(1)
keyboard.send_key('<tab>')
keyboard.send_keys('<ctrl>+v')
keyboard.send_key('<enter>')