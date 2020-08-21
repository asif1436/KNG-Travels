
from bs4 import BeautifulSoup
import requests
from django.core.files import File
def Extracts(x):
    url = 'https://en.wikipedia.org/wiki/Django_(web_framework)' #'https://www.pythonforbeginners.com/'  #'https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',

        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)

    import re
    res1 = re.findall(r'[a-zA-Z]+', output)

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    #example_sent = "This is a sample sentence, showing off the stop words filtration."

    stop_words = (stopwords.words('english'))
    words = list(open('app/common_words.txt').read().split())

    stop_words.extend(words)
    stop_words = [x.upper() for x in stop_words]
    stop_words=set(stop_words)

    #word_tokens = word_tokenize(example_sent)

    filtered_sentence = [w for w in res1 if not w in stop_words]

    filtered_sentence = []

    for w in res1:
        if w.upper() not in stop_words:
            filtered_sentence.append(w)

    from nltk.stem import PorterStemmer

    ps = PorterStemmer()

    # choose some words to be stemmed
    #words = ["program", "programs", "programer", "programing", "programers"]
    x=[]
    for w in filtered_sentence:
        x.append(ps.stem(w))

    import collections
    ctr = collections.Counter(x)
    #print("Frequency of the elements in the List : ",ctr)

    import collections
    print(collections.Counter(x).most_common(10))
