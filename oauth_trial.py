from rauth.service import OAuth1Service, OAuth1Session
from xml.dom.minidom import parseString
import configparser

class LocalLib_GRAPI():
#    def __init__(self):
#        self.gr = None
#        self.req_token = None
#        self.req_token_secret = None
#        self.session = None
    def get_oauthservice(self):
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

    def get_reqauth(self):
        self.req_token, self.req_token_secret = self.gr.get_request_token(header_auth=True)

    def get_authurl(self):
        authurl = self.gr.get_authorize_url(self.req_token)
        return authurl

    def get_session(self):
        self.session = self.gr.get_auth_session(self.req_token, self.req_token_secret)

    def get_user_info(self):
        ACCESS_TOKEN = self.session.access_token
        ACCESS_TOKEN_SECRET = self.session.access_token_secret
        username_xml = self.session.get('https://www.goodreads.com/api/auth_user')
        dom = parseString(username_xml.content)
        username = dom.getElementsByTagName('name')[0].childNodes[0].data
        userid = dom.getElementsByTagName('user')[0].getAttribute('id')
        return dom, username, userid

    #def authorizer(self):
    def __init__(self):
        self.get_oauthservice()
        self.get_reqauth()
        authorization_url = self.get_authurl()
        print('Visit this URL in your browser: ' + authorization_url)
        accepted = 'n'
        while accepted.lower() == 'n':
            accepted = input('Have you authorized me? (y/n) ')
        self.get_session()

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
