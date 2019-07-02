from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean


engine = create_engine('mysql+pymysql://root:1234567890@localhost:3306/news_orm_test?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(200), nullable=False)
    image = Column(String(300))
    author = Column(String(300))
    view_count = Column(Integer)
    created = Column(DateTime)
    is_valid = Column(Boolean)

# Base.metadata.create_all(engine)
# print("建表成功")

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(
            title='标题',
            content='内容内容内容',
            types='百家姓'
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(News).get(1)

    def get_more(self):
        return self.session.query(News).filter_by(is_valid=1)

    def updata_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        if new_obj:
            new_obj.is_valid = 0
            self.session.add(new_obj)
            self.session.commit()
            return True
        return False

    def delete_data(self, pk):
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()


def main():
    obj = OrmTest()
    # rest = obj.add_one()
    # print(rest.id, rest.title)

    # mess = obj.get_one()
    # print('ID:{0} => {1}'.format(mess.id, mess.title))

    # mess_more = obj.get_more()
    # for new_obj in mess_mo re:
    #     print('ID:{0} => {1}'.format(new_obj.id, new_obj.title))

    print(obj.updata_data(2))
    obj.delete_data(2)



if __name__ == '__main__':
    main()
