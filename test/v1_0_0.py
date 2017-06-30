# 爬虫初尝试v1.0.0
# 爬取“笔趣阁5200”首页所拥有的小说的最新一章节
# 手动修改book_name(必须是首页上出现的书)
import urllib.request
import re

website = "http://www.biquge5200.com"
my_headers = {
    'Connection': 'Keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}
req = urllib.request.Request(website, headers=my_headers)

# 修改网址首页中的书名，可以获取相应小说的最新一章节
book_name = "一念永恒"
data = urllib.request.urlopen(req).read().decode("gbk")
# print(data)r'http.*/'
reg_rule = 'href="[^>]*">' + book_name
regex = re.compile(reg_rule)
urls = re.findall(regex, data)

book_url = re.findall(r'http.*/', urls[0])
req_book = urllib.request.Request(book_url[0], headers=my_headers)
data_book = urllib.request.urlopen(req_book).read().decode('gbk')
reg_rule_book = '<dd>.*?</dd>'
regex_book = re.compile(reg_rule_book)
urls_book = re.findall(regex_book, data_book)

chapter_url = re.findall(r'http.*?.html', urls_book[0])
# print(chapter_url)
req_chapter = urllib.request.Request(chapter_url[0], headers=my_headers)
data_chapter = urllib.request.urlopen(req_chapter).read().decode('gbk')
paragraphs = re.findall(r'[\S]*<br/>', data_chapter)
for paragraph in paragraphs:
    paragraph = paragraph.replace('<br/>', '\n')
    print("  ", paragraph)

