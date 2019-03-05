from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), verbose=True)

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Query, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"), echo=True)

class GeneralQuery(Query):
    def get_by_id(self, id):
        return self.get(id)

    def find_by_filter(self, model, filter):
        query = self
        for k, v in filter.iteritems():
            query = query.filter(model.__table__.columns[k] == v)
        return query.all()

    def find_all(self, offset=0, limit=None, order=None):
        return self.order_by(order).offset(offset).limit(limit).all()


Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base(bind=engine)
Base.query = Session.query_property(GeneralQuery)
