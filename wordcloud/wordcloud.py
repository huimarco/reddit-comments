import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud.wordcloud import WordCloud, STOPWORDS

def create_wordcloud(df, image_path, random_state, output_path, figsize_x=15, figsize_y=15):
    # Put all comments from dataframe into string
    word_string = ' '.join(df['content']).lower()

    # Define stop words
    stop_words = set(STOPWORDS)

    # Set word cloud silhouette
    mask = np.array(Image.open(image_path))

    # Define wordcloud object properties
    wc = WordCloud(background_color='#282828',
                stopwords=stop_words,
                max_words=250,max_font_size=250,
                width=3000,height=3000,
                mask=mask,
                random_state=random_state)
    
    # Generate wordcloud object
    wc.generate(word_string)

    # display wordcloud object
    plt.figure(figsize=(figsize_x,figsize_y))
    plt.imshow(wc.recolor(colormap='Set2',random_state=7),interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)

    # Save the word cloud image to desktop
    plt.savefig(output_path+'wordcloud.png', bbox_inches='tight')