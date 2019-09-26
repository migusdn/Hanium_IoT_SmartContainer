import glob
import pymysql
#import cv2

# 하나씩.....
image1 = glob.glob(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test1.png')
# image2 = glob.glob(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test2.png')
# image3 = glob.glob(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test3.png')
# image4 = glob.glob(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test4.png')

end = 0

def insert_imageUrl():

    conn = pymysql.connect(host='localhost', user='root', password='1111', db ='newsc')

    curs = conn.cursor()

    sql = "insert into image values (%s)"
    curs.execute(sql, image1)
    conn.commit()
    conn.close()

def show_data():
    conn = pymysql.connect(host='localhost', user='root', password='1111', db='newsc')

    curs = conn.cursor()

    sql = "select * from image"
    curs.execute(sql)
    #이미지 실행시키는 코드
    # for i in curs.fetchone():
    #     image_view = cv2.imread(i, cv2.IMREAD_ANYCOLOR)
    #     cv2.imshow("image", image_view)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    rows = curs.fetchall()

    for i in rows:
        print(i)

    conn.close()

def delete_imageUrl():
    conn = pymysql.connect(host='localhost', user='root', password='1111', db='newsc')

    curs = conn.cursor()

    sql = "delete from image"

    curs.execute(sql)

    conn.commit()

    conn.close()

# while(end == 0):
#     quest = input('추가(a), 조회(b), 삭제(c), 종료(0) : ')
#     if(quest == 'a'):
#         a = insert_imageUrl()
#     if(quest == 'b'):
#         b = show_data()
#     if(quest == 'c'):
#         c = delete_imageUrl()
#     if(quest == '0'):

