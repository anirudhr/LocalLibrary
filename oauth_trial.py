from rauth.service import OAuth1Service, OAuth1Session
from xml.dom.minidom import parseString
import configparser

class LocalLib_GRAPI():
    def get_user_info(self):
        ACCESS_TOKEN = self.session.access_token
        ACCESS_TOKEN_SECRET = self.session.access_token_secret
        username_xml = self.session.get('https://www.goodreads.com/api/auth_user')
        dom = parseString(username_xml.content)
        username = dom.getElementsByTagName('name')[0].childNodes[0].data
        userid = dom.getElementsByTagName('user')[0].getAttribute('id')
        return dom, username, userid

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("goodreads.cfg")
        CONSUMER_KEY = config.get("Goodreads", "CONSUMER_KEY")
        CONSUMER_SECRET = config.get("Goodreads", "CONSUMER_SECRET")

        self.gr = OAuth1Service(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            name='goodreads',
            request_token_url='http://www.goodreads.com/oauth/request_token',
            authorize_url='http://www.goodreads.com/oauth/authorize',
            access_token_url='http://www.goodreads.com/oauth/access_token',
            base_url='http://www.goodreads.com/'
            )
        self.req_token, self.req_token_secret = self.gr.get_request_token(header_auth=True)
        authorization_url = self.gr.get_authorize_url(self.req_token)
        print('Visit this URL in your browser: ' + authorization_url)
        accepted = 'n'
        while accepted.lower() == 'n':
            accepted = input('Have you authorized me? (y/n) ')
        self.session = self.gr.get_auth_session(self.req_token, self.req_token_secret)


#new_session = OAuth1Session(
#    consumer_key = CONSUMER_KEY,
#    consumer_secret = CONSUMER_SECRET,
#    access_token = ACCESS_TOKEN,
#    access_token_secret = ACCESS_TOKEN_SECRET,
#)

GRAPI = LocalLib_GRAPI()
#GRAPI.authorizer()
dom, username, userid = GRAPI.get_user_info()
print('ID: %s and name: %s' % (userid, username))
