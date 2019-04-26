import pandas as pd
import re
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
#font_manager.FontProperties(fname='/usr/share/fonts/truetype/CUstomizeFonts/simhei.ttf')



def get_data(file):
    a = pd.read_csv(file,encoding='utf-8')
    a = a.loc[:,list(a.columns)[:5]]
    a.columns = ['shop_id','user_name','comment','star','timestamp']
    return a

#分词
def wordCut(data,fig=None,col='comment',backpicture = None):
    assert fig
    a = data[col].apply(lambda l: re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", str(l)))
    a = ''.join(a.tolist())
    jieba.load_userdict('./dict.txt')
    wordlist = jieba.cut(a)
    wordlist = list(filter(lambda l:len(l)>2,wordlist))
    # wordlist = list(filter(lambda l: l.encode('utf-8'), wordlist))
    # print(wordlist)
    GenerateWordCloud(wordlist,fig,backpicture)
    series = pd.Series(wordlist).value_counts(ascending=False)
    # p = series.plot('bar',title='评论')
    # plt.savefig('./analysis/'+fig+'_bar.png')
    series.to_csv('./analysis/'+fig+'_static.csv')


#生成词云
def GenerateWordCloud(word_list,fig=None,backpicture=None):
    assert fig
    if backpicture:
        background = plt.imread(backpicture)
        print('背景图片加载成功')
    else:
        background = None

    wc = WordCloud(
        width=1980,
        height=1680,
        background_color='white',
        mask=background,
        max_words=2000,
        random_state=30,
        font_path='/usr/share/fonts/truetype/CustomizeFonts/simhei.ttf'
    )
    wc.generate(' '.join(word_list))
    wc.to_file('./analysis/'+fig+'_wordcloud.png')
    print('词云保存成功')


if __name__ == '__main__':

    # file = './data/data_final.csv'
    # file = './data/都可奶茶.csv'
    # file = './data/喜茶.csv'
    file = './data/星巴克.csv'
    data = get_data(file)
    wordCut(data,'星巴克',backpicture='./resource/1.jpg')
