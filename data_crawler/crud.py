import pymysql

connection=pymysql.connect(
        host="192.168.73.128",
        port=3308,
        user="root",
        password="passw0rd!",
        database="project1",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

def insert_img_info(title, price, deal_url, img_url):
    with connection.cursor() as cursor:
        sql = '''
            INSERT INTO deal_img (title, price, deal_url, img_url)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(sql, (title, price, deal_url, img_url))
    connection.commit()

def insert_deal_info(title, price, deal_url, deal_time):
    with connection.cursor() as cursor:
        sql = '''
            INSERT INTO deal_info (title, price, deal_url, deal_time)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(sql, (title, price, deal_url, deal_time))
    connection.commit()


if __name__=="__main__":
    insert_deal_info('test', 500, 'https://www.8591.com.tw/s2233909514.html', 'https://upload.8591.com.tw/ware/20230708/1688788042929595CF.png')