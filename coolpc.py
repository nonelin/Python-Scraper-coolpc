import urllib.request
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='',database='coolpc')
insert_sql = 'INSERT INTO ssd(title) VALUES(%s)'

coolpc = urllib.request.urlopen('https://www.coolpc.com.tw/evaluate.php')
html = coolpc.read().decode("big5",errors="replace")

soup = BeautifulSoup(html, 'html.parser')
data_table = soup.select_one('#tbdy')
table_rows = data_table.select('tr')[10]
table_select = table_rows.select('.s optgroup option')

for sg in table_select:
    select_option = sg.text
    print(select_option)
    file = open("title.txt", mode="a", encoding="utf-8")
    file.write(select_option+"\n")
    file.close()
#    cursor = conn.cursor()
#    cursor.execute(insert_sql, select_option)
#    conn.commit()