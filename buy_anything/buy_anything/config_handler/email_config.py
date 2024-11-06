import os


class EmailConfig:
	BACKEND = os.environ['BUY_ANYTHING_EMAIL_BACKEND']
	USE_TLS = True if os.environ['BUY_ANYTHING_EMAIL_USE_TLS'].lower() in ['true', '1'] else False
	HOST = os.environ['BUY_ANYTHING_EMAIL_HOST']
	USER = os.environ['BUY_ANYTHING_EMAIL_HOST_USER']
	PASSWORD = os.environ['BUY_ANYTHING_EMAIL_HOST_PASSWORD']
	PORT = os.environ['BUY_ANYTHING_EMAIL_PORT']
	