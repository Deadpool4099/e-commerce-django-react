import os


class DBConfig:
	ENGINE = os.environ['BUY_ANYTHING_DB_ENGINE']
	HOST = os.environ['BUY_ANYTHING_DB_HOST']
	PORT = os.environ['BUY_ANYTHING_DB_PORT']
	USER = os.environ['BUY_ANYTHING_DB_USER']
	PASSWORD = os.environ['BUY_ANYTHING_DB_PASSWORD']
	NAME = os.environ['BUY_ANYTHING_DB_NAME']
