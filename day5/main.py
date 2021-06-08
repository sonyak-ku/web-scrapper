import requests
from flask import Flask, render_template, request

print("#######################################################################")
print("#######################################################################")
base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story&hitsPerPage=25"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story&hitsPerPage=15"



def make_detail_url(id):
    return f"{base_url}/items/{id}"

# articles 들을 쓰기 좋은 오브젝트 형식으로 반환하는 함수 만들예정


def make_article(url):
    r = requests.get(url)
    storys = r.json()
    story = []  # 스토리 이름

    for st in storys['hits']:
        storyDict = {}
        storyDict['title'] = st['title']
        storyDict['link'] = st['url']
        storyDict['point'] = st['points']
        storyDict['author'] = st['author']
        storyDict['comment'] = st['num_comments']
        storyDict['ObjID'] = st['objectID']
        story.append(storyDict)
    return story


def make_comment(url):
    r = requests.get(url)
    comments = r.json()
    comment = []  # 스토리 이름

    titleDict = {}
    commentList = []

    titleDict['title'] = comments['title']
    titleDict['link'] = comments['url']
    titleDict['point'] = comments['points']
    titleDict['author'] = comments['author']

    for child in comments['children']:
        commentDict = {}
        commentDict['name'] = child['author']
        commentDict['comment'] = child['text']
        commentList.append(commentDict)

    comment.append(titleDict)
    comment.append(commentList)

    return comment

# comment = [{title 정보}, [{'name':'comment'},{} same key repeats}]


db = {}  # comment를 id:value 의 형식으로 집어넣을 예정

app = Flask("DayNineTen")


@app.route('/')
def home():
    if request.args.get('order_by') == 'new':
        article = make_article(new)
        # 스토리 오브젝트를 리턴하는 함수가 들어가있음 좋을듯
        return render_template('index.html', number=len(article), articles=article, click=1)

    elif request.args.get('order_by') == 'popular':
        article = make_article(popular)

        return render_template('index.html', number=len(article), articles=article, click=2)
    else:
        article = make_article(popular)
        return render_template('index.html', number=len(article), articles=article, click=2)


@app.route('/<id>')
def detail(id):
    if db.get(id):
        comment = db.get(id)
        return render_template('detail.html', id=id, comment=comment)
    else:
        # false인 경우
        url = make_detail_url(id)
        comment = make_comment(url)
        db[id] = comment
        return render_template('detail.html', id=id, comment=comment)

    # 각종 코멘트들이 있는 오브젝트 반환시켜야함(함수를 적는게 나음)

# 링크를 클릭하면 댓글 창으로 가는 기능은 redirect 사용인가?


app.run(host="0.0.0.0")

# 커멘트들 깔끔하게 뽑기, 클릭했을때 글자 검은색으로 변하게 파퓰러뉴
