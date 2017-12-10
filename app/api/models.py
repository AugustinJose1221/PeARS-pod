from app import db
from app.utils import readDM

#Build semantic spaces
dm_dict_en = readDM("./app/static/spaces/english.dm")


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Pods(Base):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(1000))
    description = db.Column(db.String(7000))
    language = db.Column(db.String(1000))

    def __init__(self, url=None, description=None, language=None):
        self.url = url
        self.description = description
        self.language = language

class Urls(Base):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(1000))
    title = db.Column(db.String(1000))
    vector = db.Column(db.String(7000))
    freqs = db.Column(db.String(7000))
    snippet = db.Column(db.String(1000))
    cc = db.Column(db.Boolean)

    def __init__(self, url=None, title=None, vector=None, freqs=None, snippet=None, cc=False):
        self.url = url
        self.title = title
        self.vector = vector
        self.freqs = freqs
        self.snippet = snippet
        self.cc = cc

    def __repr__(self):
        return self.url

    @property
    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'title': self.title,
            'vector': self.vector,
            'freqs': self.freqs,
            'snippet': self.snippet,
            'cc': self.cc
        }
