import os

DEBUG = False

SITE_NAME = "Medeco Dashboard"
SITE_AUTHOR = "Ronald Bruintjes"
SITE_URL = "http://medeco-stashboard.appspot.com"
REPORT_URL = "mailto:helpdesk@medeco.com"

# Twitter update settings
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_HANDLE = 'stashboard_status'

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
