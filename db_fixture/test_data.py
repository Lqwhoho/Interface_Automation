import sys
import time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB


# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-100000))

# 定义当前时间
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+10000))


# 创建测试数据
datas = {
    # 发布会表数据
    'sign_event': [
                   {'id': 1, 'name': '华为发布会', '`limit`': 20000, 'status': 1,
                    'address': '深圳', 'start_time': future_time, 'create_time': current_time},
                   {'id': 2, 'name': '可参加人数Wi为0', '`limit`': 0, 'status': 1,
                    'address': '洛杉矶', 'start_time': future_time, 'create_time': current_time},
                   {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0,
                    'address': '北京会展中心','start_time': future_time, 'create_time': current_time},
                   {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1,
                    'address': '北京会展中心','start_time': past_time, 'create_time': current_time},
                   {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1,
                    'address': '北京国家会议中心', 'start_time': future_time, 'create_time': current_time},
                   ],
    # 嘉宾表数据
    'sign_guest': [
                  {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0,
                   'event_id': 1},
                  {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1,
                   'event_id': 1},
                  {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0,
                   'event_id': 5},
                  ],
        }


# 插入数据
def init_data():
    """
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()
    """
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
