# Word_Cloud

This script generates word cloud for the novel Treasure Island by Robert Louis Stevenson. This code can be used to generate word cloud for other texts as well.  

Though it was not required but I used the NLTK library to do the following tasks:

  1. Tokenize the text
  2. Removed punctuation 
  3. Removed all the stop words (Using gensim stop words)
  4. Removed All the Digits
  5. I also created a custom list of words to remove more words
 
After that I created a dictionary to count the frequency of words.
The Word Cloud was then generated using the wordcloud library.
