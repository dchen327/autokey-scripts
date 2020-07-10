'''
Launch various websites stored in urls
'''
import webbrowser
urls = ['messenger.com', 'discord.com/app']
webbrowser.open_new(urls[0])
for url in urls[1:]:
    webbrowser.open_new_tab(url)