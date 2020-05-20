from PIL import Image
import numpy as np
import wordcloud, codecs
import MeCab

file = codecs.open('diary-202004.txt','r', 'utf-8', 'ignore')
text = file.read()
# msk = np.array(Image.open('app-visual-0.png'))

m = MeCab.Tagger('')
text = text.replace('\r','')
parsed = m.parse(text)

#助詞、助動詞を除いて単語結合
splitted = ' '.join([x.split('\t')[0] for x in parsed.splitlines()[:-1] if x.split('\t')[1].split(',')[0] not in ['助詞', '助動詞']])

wordc = wordcloud.WordCloud(
        font_path='RiiTN_R.otf',
        background_color='white',
        # mask=msk,
        contour_color='steelblue',
        width=800,
        height=600,
        contour_width=2).generate(splitted)
wordc.to_file('summary-202004.png')
