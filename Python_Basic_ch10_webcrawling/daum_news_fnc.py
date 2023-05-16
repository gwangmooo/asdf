import requests
from bs4 import BeautifulSoup


#input: URL
#output: 제목, 본문

# 기존: 제목함수, 본문함수
# -> 이유: 함수만들때 하나의 함수에 다수의 기능을 넣기 X

def get_news_title_and_content(url):

    result = requests.get(url)
    print(result)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")  # section 태그 안에 있는 p태그들
    content = ""
    # contents.pop(-1)

    for tag in contents:
        content = content + tag.get_text()
    print(f"뉴스본문: {content}")

    return title, content























