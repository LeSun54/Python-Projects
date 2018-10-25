import urllib.request
import urllib.parse

def read_text():
    quotes = open(r"C:\Users\Leon\Downloads\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    encoded_text = urllib.parse.quote(text_to_check)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+encoded_text)
    output = connection.read()
    print(output)
    connection.close()
    if b"true" in output:
        print("Profanity Alert")
    elif b"false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    
read_text()
