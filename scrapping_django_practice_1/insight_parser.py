import requests
from bs4 import BeautifulSoup
import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from scrapping.models import Press, Category, Article
import datetime

insight_news_info = []
    
# Dict형태로 변환 함수
def dict_infor(**kwargs):
    context = {}
    for k,v in kwargs.items():
        context[k] = v
    
    return context

def parse_insight():
    cnt = 0 # 뉴스 number
    data = {}
    i = 0

    try:
        for num in range(1,20):
            response = requests.get(f'https://www.insight.co.kr/section/health?page={num}')
            soup = BeautifulSoup(response.text, 'html.parser')

            ul = soup.select_one('body > div.content > div > div.section-wrap > div.section-list > ul')
            lis = ul.select('li')
            category = soup.select_one('body > div.content > div > div.section-wrap > div.section-gnb > span')
            press = soup.select_one('body > div.content > div > div.section-wrap > div.section-gnb > a').text
        
            for li in lis:
                cnt += 1
                preview_img = li.select_one('li > div > a.section-list-article-image')
                preview_img = preview_img['style'].split("(")[1].split(')')[0]
                print(preview_img)
                title = li.select_one('li > div > a.section-list-article-title').text.strip()
                news_category = category.text.split('>')[1].strip()
                date = li.select_one('li > div > span.section-list-article-byline')
                link = li.select_one('li > div > a.section-list-article-title')['href']
                code = link.split('/')[4]

                news_url = requests.get(link)
                news_url_html = BeautifulSoup(news_url.text, 'html.parser')
                
                content = news_url_html.select_one('body > div.content > div > div.news-container > div.news-wrap > div.news-article > div.news-article-memo')
                news_image = content.select('img')
                image_url_list = []
                
                for image in news_image:
                    image_url_list.append(image['src'])
                
                if '·' in date.text:
                    date = date.text.strip().split('·')[1]

                else:
                    date = date.text.strip()
                date_code = date.replace(' ','-').split('-')
                date_code = ' '.join(date_code).split()
                date_code = date_code[0]+'-'+date_code[1]+'-'+date_code[2]+' '+date_code[3]
                print(date_code)
                # date_code = datetime.datetime.strptime(date_code,'%Y%m%d%H%M%S')
    #         print(datetime.datetime.strptime(date_list,'%Y%m%d%H%M%S'))
                insight_news_info = dict_infor(press=press,news_code=code, news_category=news_category, date=date, date_code=date_code, preview_img=preview_img, title=title, content=content.text,img=image_url_list,ref=link )
                print(insight_news_info)            
                i += 1
                data[i] = insight_news_info
        return data
    except:
        pass
        # except:
        #     print('문제가 있네용')
        #     pass

if __name__=='__main__':

    news_dict = parse_insight()

    try:
        for v in news_dict.values():
            if not Article.objects.filter(title = v['title']):
                Article.objects.create(
                    press=Press.objects.filter(name=v['press']).first(),
                    category=Category.objects.filter(name=v['news_category']).first(),
                    code=v['news_code'],
                    date=v['date'],
                    date_code=v['date_code'],
                    preview_img=v['preview_img'],
                    title=v['title'],
                    img=v['img'],
                    content=v['content'],
                    ref=v['ref']
                    )
    except:
        pass
