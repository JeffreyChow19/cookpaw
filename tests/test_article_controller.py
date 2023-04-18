# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from controller.controller import *
from models.article import *

def test_article_controller():
    # make a new controller
    controller = Controller("src/database/cookpaw.db")
    article = {
        "title" : "Article Title",
        "content" : "Article Content",
    }

    # insert new article
    controller.create_article(article)

    # get all articles
    articles = controller.get_all_articles()

    # get recently inserted article
    last_article = articles[-1]

    # TEST: get_article_by_id
    last_article_by_id = controller.get_article_by_id(last_article.article_id)
    assert last_article_by_id[0] == last_article.article_id

    # TEST: update_article
    updated_article = {
        "title" : "Updated Article Title",
        "content" : "Article Content",
    }
    controller.update_article(last_article.article_id, updated_article)
    articles = controller.get_all_articles()
    last_article = articles[-1]

    assert last_article.title == updated_article["title"]
    assert last_article.title != article["title"]
    assert last_article.content == updated_article["content"]


    # delete last inserted article, resets the db
    controller.delete_article(last_article.article_id)

    # get last article after deletion of last_article
    articles = controller.get_all_articles()
    last_article_after_del = articles[-1]

    # TEST: create_article, get_all_articles, delete_article
    assert last_article.title == updated_article["title"]
    assert last_article.content == updated_article["content"]
    assert last_article_after_del.title != updated_article["title"]
    assert last_article_after_del.content != updated_article["content"]
