from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist=fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase count of that word by 1
            worddictionary[word] += 1
        else:
            #add that word to the dictionary.
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist), 'wordlist':sortedwords})

# The list being put in includes non alphabetic characters. This can be remedied with regular expressions but I'm not too great at regex.

def about(request):
    return render(request, 'about.html')
