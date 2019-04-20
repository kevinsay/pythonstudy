import sqlalchemy
import pymysql

from sqlalchemy import Column, Integer, String, DATE, Enum, Table, MetaData, ForeignKey
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker, relationship

# mysql+pymysql://用户名:密码@主机/库名
engineer = create_engine("mysql+pymysql://root:shiyutao2012@localhost/shiyutao", encoding='utf-8', echo=False)
# echo=True:打印orm执行的sql语句

# 基类
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '%s %s' % (self.id, self.name)


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("m", "f"), nullable=False)


class StudyRecord(Base):
    __tablename__ = "studyrecord"
    id = Column(Integer, primary_key=True)
    day = Column(String(10), nullable=False)
    status = Column(String(32), nullable=False)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", backref="my_study_record")

    def __repr__(self):
        return '%s,%s,%s' % (self.student.name, self.day, self.status)


# 创建表结构
# Base.metadata.create_all(engineer)
# exit()

Session_class = sessionmaker(bind=engineer)  # 创建与数据库的会话Session Class
session = Session_class()
# 增
# user_obj1 = User(name='alex',password='123456')
# session.add(user_obj1)
#
# session.commit()
# 查询
# data = session.query(User).filter_by(id=1).all()
# print(data[0].name)

# data = session.query(User).filter_by().all()
# data = session.query(User).filter_by(id=1).first()

# data = session.query(User).filter(User.id==1).first()
# print(data)

# 修改
# data.name = 'shiyt'
# session.commit()

# fake_user = User(name='fuck', password='111111')
# session.add(fake_user)
# add之后commit之前query可以查询到新添加的对象
# print(session.query(User).filter_by(name='fake').first())
# 但是在commit之前进行rollback就查询不到了
# session.rollback()
# print(session.query(User).filter_by(name='fake').first())

#
# session.commit()
# 统计
# print(session.query(User).filter_by(password='123456').count())
# # 分组
# print(session.query(User.name, func.count(User.name)).group_by(User.name).all())

# 删除
# del_user = session.query(User).filter_by(name='shiyt').first()
# session.delete(del_user)
# session.commit()
# print(session.query(User).filter_by(name='shiyt').all())

# student = Student(name='shiyutao',register_date='2019.03.27',gender='m')
# session.add(student)
# session.commit()

# 关联查询
# print(session.query(User, Student).filter(User.id > Student.id).all())
# print(session.query(User).join(Student).all())

# 批量添加
# s1 = Student(name="a1", register_date="2019-03-28", gender='f')
# s2 = Student(name="a2", register_date="2019-03-28", gender='m')
# s3 = Student(name="a3", register_date="2019-03-28", gender='f')
# s4 = Student(name="a4", register_date="2019-03-28", gender='f')
#
# study_record1 = StudyRecord(day='1', status='Yes', student_id=1)
# study_record2 = StudyRecord(day='2', status='Yes', student_id=1)
# study_record3 = StudyRecord(day='3', status='Yes', student_id=1)
#
# study_record4 = StudyRecord(day='1', status='Yes', student_id=2)
# study_record5 = StudyRecord(day='2', status='Yes', student_id=2)
# study_record6 = StudyRecord(day='3', status='Yes', student_id=2)
#
# session.add_all([s1, s2, s3, s4])
# session.add_all([study_record1, study_record2, study_record3, study_record4, study_record5, study_record6])
# session.commit()

student = session.query(Student).filter(Student.name == 'a1').first()
print(student.my_study_record)

# metadata = MetaData()
# user1 = Table('user1', metadata,
#              Column('id', Integer, primary_key=True),
#              Column('name', String(50)),
#              Column('gender', String(20)))

# class User:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# mapper(User, user1)
