from application.base import mysql_db
from application.base.redPrint import RedPrint
from application.api_v1.model.weiboModel import WeiboUser, WeiboComment
import pymongo
api = RedPrint('weibo')

@api.route('/test3', methods=['GET'])
def test3():
    users = WeiboUser.query.all()
    print(users)
    results =[]
    gender_map={'f':1,'m':0}
    for user in users:
        item={}
        gender = user.__dict__.get('gender')
        if gender is None:
            continue
        item['gender'] = gender_map[gender]
        item['username'] = user.__dict__.get('username')
        if '用户' in item['username']:
            continue
        print(item)
        results.append(item)
    import pandas as pd
    pd.DataFrame(results).to_csv('gender.csv')
    return 'ok'

@api.route('/test2', methods=['GET'])
def test2():
    myclient = pymongo.MongoClient("mongodb://user:32SZnr518000@139.159.204.92:27017/")
    db = myclient["spiderServer"]
    users = []
    set_uid = set()
    for row in list(db['weibo_users3'].find()):
        user = WeiboUser()
        user.url = row.get('url')
        user.username = row.get('username')
        user.following = row.get('following')
        user.uid = row.get('uid')
        if user.uid in set_uid:
            continue
        else:
            set_uid.add(user.uid)
        user.birthday = row.get('birthday')
        user.followed = row.get('followed')
        user.gender = row.get('gender')
        user.edu = row.get('edu')
        user.location = row.get('location')
        user.post_num = row.get('post_num')
        user.url = row.get('url')
        users.append(user)

    comments = []
    set_com=set()
    for row in list(db['weibo_comments3'].find()):
        item = WeiboComment()
        item.item_id = row.get('item_id')
        item.comment_id = row.get('comment_id')
        if item.comment_id in set_uid:
            continue
        else:
            set_com.add(item.comment_id)

        item.createtime = row.get('createtime')
        item.text = row.get('text')
        item.uid = row.get('uid')
        item.like_count = row.get('like_count')

        comments.append(item)
    batch_step = 1000
    # for index in range(0, len(users), batch_step):
    #     item_list = users[index:index + batch_step]
    #     mysql_db.session.add_all(item_list)
    #     mysql_db.session.commit()

    for index in range(0, len(comments), batch_step):
        item_list = comments[index:index + batch_step]
        mysql_db.session.add_all(item_list)
        mysql_db.session.commit()

    return 'ok'


