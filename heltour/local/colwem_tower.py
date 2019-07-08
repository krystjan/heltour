DEBUG = True
GOOGLE_SERVICE_ACCOUNT_KEYFILE_PATH = '/home/colwem/workshop/heltour/.ignore/conf/gspread.conf'
SLACK_API_TOKEN_FILE_PATH = '/home/colwem/workshop/heltour/.ignore/conf/slack-token.conf'
SLACK_WEBHOOK_FILE_PATH ='/home/colwem/workshop/heltour/.ignore/conf/slack-webhook.conf'
LICHESS_CREDS_FILE_PATH = '/home/colwem/workshop/heltour/.ignore/conf/lichess.conf'
LINK_PROTOCOL = 'http'
SITE_ID = 1

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
JAVAFO_COMMAND = 'java -jar /home/colwem/workshop/heltour/.ignore/javafo.jar'
STATIC_ROOT = '/home/colwem/workshop/heltour/heltour/tournament/static'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SLACK_HOST = 'zhteamtesting.slack.com'
BOT_USER_ID = 'UGSUFP605'
BOT_NAME = 'crazybot'
TASK_SERIALIZER = 'json'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
    # root logger
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
}
