import pymysql

class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                passwd='1234567890',
                db='news',
                port=3306,
                charset='utf8'
            )
        except pymysql.Error as e:
            print("error: %s" % e)

    def close_conn(self):
        try:
            if self.conn:
                # 关闭链接
                self.conn.close()
        except pymysql.Error as e:
            print("error: %s" % e)

    # 查询一条数据
    def get_one(self):
        sql = 'SELECT * FROM `news`'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # rest = cursor.fetchall()
        cursor.close()
        self.close_conn()
        return rest

    # 查询多条数据
    def get_more(self):
        sql = 'SELECT * FROM `news`'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    # 写入一条数据
    def add_one(self):
        try:
            sql = "INSERT INTO `news` (`title`, `content`, `created`, `image`, `types`, `is_valid`) VALUE ('新增标题', '新添加', '2019-12-12 12:12:12' ,'imageNew', 'typesss', 1)"
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
            cur.close()
            print("写入 OK")
        except:
            self.conn.rollback()
        self.close_conn()

def main():

    obj = MysqlSearch()
    # obj.add_one()
    res = obj.get_one()
    print(res)
    # res_more = obj.get_more()
    # print(res_more)

if __name__ == '__main__':
    main()
