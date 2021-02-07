import urllib.parse, urllib.request, re
import random


def get_youtube_data(term):
    query_string = urllib.parse.urlencode({'search_query': term})
    htm_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})',
                                htm_content.read().decode())
    return 'http://www.youtube.com/watch?v=' + search_results[0]


def choose_word(string):
    list_of_words = string.split()
    return f"MyChoice is: ***{random.choice(list_of_words)}***"
