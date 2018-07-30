from flask import request, jsonify, g
from . import apiv1
from ..models.feed import Feed
from app import db
from .auth import login_required
from ..schema.news_schema import *
from .api_helper import *

class FeedController():
    def __init__(self):
        ''''''

    @staticmethod
    @login_required
    def index():
        '''Returns all the news for a user
        Call this api passing a user key
        ---

        responses:
          500:
            description: Error The language is not awesome!
          200:
            description: A language with its awesomeness
            schema:
              id: News
              properties:
                title:
                  type: string
                  description: The article name
                  default: None
                image:
                  type: base/64
                  description: Image representing the news item

                  '''

        feed = db.session.query(Feed).all()
        return common_response(object=newses_schema.dump(feed))



    @staticmethod
    @login_required
    def search():
        '''Create a news for a user
                Call this api passing a user key
                ---

                responses:
                  500:
                    description: Meh, we're broken!
                  200:
                    description: News created!
                    schema:
                      id: awesome
                      properties:
                        title:
                          type: string
                          description: The article name
                          default: None
                        image:
                          type: base/64
                          description: Image representing the news item

                          '''

        req_data = request.get_json()

        news = Feed.search(q=req_data["q"], user_id=g.user.id)

        return common_response(object=newses_schema.dump(news))


