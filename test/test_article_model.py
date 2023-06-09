# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from models.article import *

def test_article_model():
    title = "Article Title"
    content = "Article Content"
    author = "Article Author"
    publish_date = "Article Publish Date"
    path = "Article Image Path"

    a = Article(0, title, content, author, publish_date, path)

    assert a.article_id == 0
    assert a.title == title
    assert a.content == content
    assert a.publish_date == publish_date
    assert a.author == author
    assert a.image_path == path
