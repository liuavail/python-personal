import requests
from bs4 import BeautifulSoup
import json

#下载所有页面的html
def download_all_htmls():
    '''下载所有列表页面的html，用于后续的分析'''
    htmls = []
    for page in range(42):
        url = f"http://www.crazyant.net/page/{page+1}"
        #print("craw html:",url)
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls

#执行爬取
htmls = download_all_htmls()

#解析html得到数据
def parse_single_html(html):
    """
    解析单个html得到数据，
    return list（link，title，label）
    """
    soup = BeautifulSoup(html,'html.parser')
    articles = soup.find_all("article")
    datas = []
    for article in articles:
        #查找超链接
        title_node = (
            article.find("h2",class_="entry-title").find("a")
        )
        title = title_node.get_text()
        link = title_node["href"]

        #查找标签列表
        tag_node = (
            article
                .find("header",class_="entry-header")
                .find("span",class_="cat-links")
                .find("a")
        )
        tags = tag_node.get_text()
        
        datas.append({"title":title,"link":link,"tags":tags})
    return datas 



#执行所有html页面解析
all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))

#将结果输出存储
with open("all_article_links.json","w") as fout:
    for data in all_datas:
       fout.write(json.dumps(data,ensure_ascii=False)+"\n")