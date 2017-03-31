"""
Programma per ricevere una lista di parole da un sito e stamaprle
USAGE: python words.py <URL>
"""
import urllib2
import sys

def fetch_words(url):

    """
    Questo e' il modulo di raccolta
    :param url: Indirizzo url del sito  http://sixty-north.com/c/t.txt
    :return: List of words from the text file
    """
    # story = urllib2.Request('http://sixty-north.com/c/t.txt')
    story = urllib2.Request(url)
    response = urllib2.urlopen(story)
    story_words = []
    for line in response:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    return story_words

def print_items(items):
    """
    Stampa ogni parola trovata nel testo dricevuto
    :param items: Lista delle parole ricevute
    :return: Niente
    """
    for item in items:
        print(item)

def main(url):
    """
    Print each word from a tect codument from a URL
    :param url: THE ULR OFA UTF-8 text document
    :return:
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
   main(sys.argv[1])