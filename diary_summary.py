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

# ストップワードの設定
stop_words = [ u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
             u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
             u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
             u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'あり', u'ため', u'この', u'なり', u'しまっ', \
             u'なっ', u'いっ', u'どう', u'たち', u'いく', u'こう', u'その', u'やっ', u'あっ', u'でき', u'いき',\
             u'より', u'いき', u'すん', u'かかっ', u'しよ', u'もん', u'あと', u'すぎ', u'さす', u'くれ']

#助詞、助動詞を除いて単語結合
splitted = ' '.join([x.split('\t')[0] for x in parsed.splitlines()[:-1] if x.split('\t')[1].split(',')[0] not in ['助詞', '助動詞']])

wordc = wordcloud.WordCloud(
        font_path='RiiTN_R.otf',
        background_color='white',
        # mask=msk,
        # contour_width=4,
        contour_color='steelblue',
        width=800,
        height=600,
        # regexp="[\w']+",
        stopwords=set(stop_words)).generate(splitted)
wordc.to_file('summary.png')
