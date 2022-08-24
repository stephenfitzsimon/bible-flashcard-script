from urllib import error, parse, request
import sys
import json

def main():
    print('Welcome to the bible flashcard maker\nPlease enter the following information:\n')
    book = input('Book: ')
    chapter = input('Chapter: ')
    verse = input('Verses: ')
    url = build_api_query(book, chapter, verse)
    verses = get_bible_request(url)
    string_verse = make_cs_strings(verses)
    see = input('Would you like to see the verses? [Y/n] ')
    if see=='Y':
        print(string_verse)
    make_file = input('\nDo you want to make the flashcard file? [Y/n] ')
    if make_file == 'Y':
        made_file = make_anki_file(string_verse)
    if made_file:
        print('File made! Thanks!')

def build_api_query(book, chapter, verses):
    """"
    Builds a url for the labs.bible.org api.  Will pass plain formatting and as for a json
    """
    base_url = 'http://labs.bible.org/api/?passage='
    verse_call = f"{book}+{chapter}:{verses}"
    url = base_url + verse_call + "&formatting=plain&type=json"
    return url
    
def get_bible_request(url):
    try:
        response = request.urlopen(url)
    except error.HTTPError as http_error:
        if http_error.code == 401: #access denied error code
            sys.exit('Access Denied. Check API key')
        elif http_error.code == 404: #404 not found
            sys.exit('Can''t find verse') 
        else:
            sys.exit(f'Something went wrong... ({http_error.code})')
    verse = response.read()
    try:
        return json.loads(verse) #return a python object holding JSON data
    except json.JSONDecodeError: 
        #python could not correctly read the server response
        sys.exit('Couldn''t read server response')

def make_cs_strings(verses):
    formatted_string = ""
    for v in verses:
        v_str = f"{v['bookname']} {v['chapter']}:{v['verse']}\t{v['text']}\n"
        formatted_string += v_str
    return formatted_string

def make_anki_file(format_string):
    with open('cards.txt', 'w') as f:
        f.write(format_string)
    return True

if __name__=='__main__':
    main()