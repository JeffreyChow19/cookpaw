# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from controller.controller import *
from models.article import *

def test_article_controller():
    article = {
        "title" : "Article Title",
        "content" : "Article Content",
    }
    controller = Controller("src/database/cookpaw.db")

    controller.create_article(article)

    articles = controller.get_all_articles()

    last_article = articles[-1]

    controller.delete_article(last_article.article_id)

    articles = controller.get_all_articles()
    last_article_after_del = articles[-1]

    assert last_article.title == article["title"]
    assert last_article.content == article["content"]
    assert last_article_after_del.title != article["title"]
    assert last_article_after_del.content != article["content"]