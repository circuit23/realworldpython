import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


# Load a text file as a string.
with open('hound.txt') as infile:
    text = infile.read()

# Lead an image as a NumPy array.
mask = np.array(Image.open('holmes.png'))

# Get stop words as a set and add extra words.
stopwords = STOPWORDS
stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may', 'little', 'say', 'must', 'way', 'long',
                  'yet', 'mean', 'put', 'seem', 'asked', 'made', 'half', 'much', 'certainly', 'might', 'came'])

wc = WordCloud(max_words=500,
               relative_scaling=0.5,
               mask=mask,
               background_color='white',
               stopwords=stopwords,
               margin=2,
               random_state=7,
               contour_width=2,
               contour_color='brown',
               colormap='copper').generate(text)

colors = wc.to_array()
