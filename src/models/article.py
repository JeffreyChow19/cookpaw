from models.model import *
class Article(Model):
    def __init__(self, article_id, title, content, author, publish_date, path):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author = author
        self.publish_date = publish_date
        self.image_path = path
    