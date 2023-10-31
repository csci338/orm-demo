# https://mattermost.com/blog/building-a-crud-fastapi-app-with-sqlalchemy/
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()


url = URL.create(
    drivername="postgresql",
    username=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=os.environ.get('DB_PORT'),
    database=os.environ.get('DB_NAME')
)

# engine = create_engine(url, echo=True)
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
