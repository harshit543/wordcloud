from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image

#Content-related
text = open('spiderman.txt', 'r').read()
stopwords = set(STOPWORDS)

#Appearance-related
custom_mask = np.array(Image.open('thor.jpg')) 
wc = WordCloud(background_color = 'white',
               stopwords = stopwords,
               mask = custom_mask,
               contour_width = 3,
               contour_color = 'black')

wc.generate(text)


#Plotting
##plt.imshow(wc, interpolation = 'bilinear')
##plt.axis('off')
##plt.show()

wc.to_file('thor2.jpg')

