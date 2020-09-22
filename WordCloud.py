f = open(".../lincoln_TemperanceAddress.txt","r",encoding="utf-8")
myText = f.readlines()
myText = "".join(myText)
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
wordcloud = WordCloud(background_color='white').generate(myText)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()