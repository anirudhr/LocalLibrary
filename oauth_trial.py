from rauth.service import OAuth1Service, OAuth1Session
from xml.dom.minidom import parseString
import configparser

def get_oauthservice():
    config = configparser.ConfigParser()
    config.read("goodreads.cfg")
    CONSUMER_KEY = config.get("Goodreads", "CONSUMER_KEY")
    CONSUMER_SECRET = config.get("Goodreads", "CONSUMER_SECRET")

    gr = OAuth1Service(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        name='goodreads',
        request_token_url='http://www.goodreads.com/oauth/request_token',
        authorize_url='http://www.goodreads.com/oauth/authorize',
        access_token_url='http://www.goodreads.com/oauth/access_token',
        base_url='http://www.goodreads.com/'
        )
    return gr

def get_reqauth(gr):
    req_token, req_token_secret = gr.get_request_token(header_auth=True)
    return (req_token, req_token_secret)

def get_authurl(gr, reqtoken):
    authurl = gr.get_authorize_url(reqtoken)
    return authurl

goodreads = get_oauthservice()
request_token, request_token_secret = get_reqauth(goodreads)
authorization_url = get_authurl(goodreads, request_token)


print('Visit this URL in your browser: ' + authorization_url)
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = input('Have you authorized me? (y/n) ')

session = goodreads.get_auth_session(request_token, request_token_secret)
ACCEESS_TOKEN = session.access_token
ACCESS_TOKEN_SECRET = session.access_token_secret

#new_session = OAuth1Session(
#    consumer_key = CONSUMER_KEY,
#    consumer_secret = CONSUMER_SECRET,
#    access_token = ACCEESS_TOKEN,
#    access_token_secret = ACCESS_TOKEN_SECRET,
#)

username_xml = session.get('https://www.goodreads.com/api/auth_user')
dom = parseString(username_xml.content)
username = dom.getElementsByTagName('name')[0].childNodes[0].data
print('Username: %s' % username)
