# 爬虫v1.0.1
# 爬取“笔趣阁5200”首页所拥有的小说的最新一章节
# 在v1.0.0的基础上，整理相关模块，修改html文本解码部分
import urllib.request
import re
import chardet

def get_html_text(url):
    my_headers = {
        'Connection': 'Keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=my_headers)
    response = urllib.request.urlopen(request)
    # print(response)
    response_body = response.read()
    encoding = chardet.detect(response_body)['encoding']
    if encoding != 'utf-8' or encoding != 'UTF-8':
        encoding = 'gbk'
    response_body = response_body.decode(encoding)
    # print(response_body)
    return response_body

def get_url(re_rule, html_text):
    regex = re.compile(re_rule)
    urls = re.findall(regex, html_text)
    if len(urls) == 0:
        return None
    else:
        return urls[0]

def get_chapter_text(html_text):
    regex = r'[\S]*<br/>'
    paragraphs = re.findall(regex, html_text)
    for paragraph in paragraphs:
        paragraph = paragraph.replace('<br/>', '\n')
        print("  ", paragraph)

def get_latest_chapter(book_name, url="http://www.biquge5200.com"):
    main_page = get_html_text(url)
    regx = 'href="[^>]*">' + book_name
    book_url = get_url(regx, main_page)
    if book_url:
        book_url = get_url(r'http.*/', book_url)
        book_page = get_html_text(book_url)
        regex_chapters = '<dd>.*?</dd>'
        chapter_url = get_url(regex_chapters, book_page)
        chapter_url = get_url(r'http.*?.html', chapter_url)
        chapter_page = get_html_text(chapter_url)
        get_chapter_text(chapter_page)
    else:
        print("网站首页无此书")

get_latest_chapter("一念永恒")

