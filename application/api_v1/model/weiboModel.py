# -*- ecoding: utf-8 -*-
# @ModuleName: weiboModel
# @Author: jason
# @Email: jasonforjob@qq.com
# @Time: 2021/5/8 18:25
# @Desc:
from sqlalchemy import Column, String, Integer

from application.base import mysql_db as db


class Test(db.Model):
    # 定义表名
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    test = db.Column(db.String(255))
    ss = db.Column(db.String(255))

class WeiboUser(db.Model):
    # 定义表名
    __tablename__ = 'weibo_user'
    # 定义字段
    uid = Column(String(255), primary_key=True)
    username = Column(String(255))
    url = Column(String(255))
    following = Column(Integer())
    followed = Column(Integer())
    gender = Column(String(255))
    edu = Column(String(255))
    birthday = Column(String(255))
    post_num = Column(Integer())
    age = Column(Integer())
    star = Column(String(255))
    province = Column(String(255))
    district = Column(String(255))
    edu_tag = Column(String(255))
    edu_level =Column(String(255))

class WeiboComment(db.Model):
    # 定义表名
    __tablename__ = 'weibo_comment'
    # 定义字段
    comment_id = db.Column(db.String(255), primary_key=True)
    item_id = db.Column(db.String(255))
    uid = db.Column(db.String(255))
    createtime = db.Column(db.String(255), unique=True, index=True)
    text = db.Column(db.TEXT())
    like_count = db.Column(db.Integer())


