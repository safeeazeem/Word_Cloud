import nltk
import io
import os
import string
import re
import gensim
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
from matplotlib import pyplot as plt
import wordcloud


#Change the name of the file_1 to the text file you want to generate the word cloud for.
file_1 = 'Treasure_island.txt'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, file_1)


'''
    To remove additional words, just add them to the remove list
    The frequency dictionary stores the frequency of words.
'''

def Generate_Word_Cloud(file):
    text = open(file,encoding="utf8").read()
    tokens = nltk.word_tokenize(text.lower())
    pattern = '[0-9]'
    remove = ["'s", '.', '--','','__','oh', "'re",'”','“',"'t","n't","'m","'nt","'ve","'ll",'said', 'mr.','replied','mrs.']
    no_punc = [word for word in tokens if word not in string.punctuation]
    no_num = [re.sub(pattern, '',word)for word in no_punc ]
    no_stop = [word for word in no_num if word not in all_stopwords]
    clean = [word for word in no_stop if word not in remove]

    frequencies = {}
    for word in clean:
        frequencies[word]=frequencies.get(word,0)+1

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()



myimage = Generate_Word_Cloud(my_file)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
