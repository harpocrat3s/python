#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# This is the final project of a Google Python course I did some time ago on Coursera. The script
# was done in a Jupyter book, part of the code was already provided by the instructors. 
# Here's the assignment:

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs 
# to process the text, remove punctuation, ignore case and words that do not contain all alphabets, 
# count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of 
# the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your 
# dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the 
# text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [
# Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  
# You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by 
# Jane Austen. Save this as a .txt file somewhere on your computer.
# 
# You will need to upload your input file here so that your script will be able to process it.  
# To do the upload, you will need an uploader widget.  


get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys



# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* 
# that your word cloud script can process. 


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     
                            "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", 
                            "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", 
                            "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had",  
                            "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     
                            "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", 
                            "very", "can", "will", "do", "just"]
    
    splitted_list = file_contents.split()
    
    words_dictionary = {}
    for word in splitted_list:
        temp_word = word
        for char in punctuations:
            if char in word:
                temp_word = word.replace(char, '')
                
        temp_word = temp_word.lower()
        if temp_word not in uninteresting_words:
            if temp_word not in words_dictionary:     
                words_dictionary[temp_word] = 1
            else:
                words_dictionary[temp_word] = words_dictionary[temp_word] + 1
            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_dictionary)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
