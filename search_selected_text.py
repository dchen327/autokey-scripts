'''
Search currently highlighted text
'''
import webbrowser
base = "http://www.google.com/search?q="
phrase = clipboard.get_selection()

# Remove trailing or leading white space and find if there are multiple words.
phrase = phrase.strip()
search_url = base + phrase
webbrowser.open(search_url)
