import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# エンジンの作成
engine = sqlalchemy.create_engine('sqlite:///:memory:')

# Baseクラスの作成
Base = declarative_base()

# Personクラスの定義
class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

# テーブルの作成
Base.metadata.create_all(engine)
