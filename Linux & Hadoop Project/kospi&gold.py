import mysql.connector
import  pandas as  pd
import matplotlib.pyplot as plt

config = { 
    "user": "root", 
    "password": "-", 
    "host": "192.168.56.101", #local
    "database": "orcl", #Database name 
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306) 
} 


conn = mysql.connector.connect(**config)

# db select, insert, update, delete 작업 객체
cursor = conn.cursor()

# 실행할 select 문 구성
sql = """
select sum(value)/sum(*)
from kospi”””
sql = """select sum(PriceUSDperOz)/sum(*) from gold"""     
           
# sql 을 실행해서 cursor (메모리) 에 담는다. 
cursor.execute(sql)

# cursor(메모리)에 담긴 결과 셋 얻어오기
resultList = cursor.fetchall()  # tuple 이 들어있는 list
df = pd.DataFrame(resultList)  # 판다스 데이터 프레임으로 변환 
df.columns = ['years', 'value']   #  컬럼명을 만들어 줍니다. 
print(df[['years', 'value']])


# 시각화 
years = [
  '1990~', '1995~', '2000~', '2005~', '2010~', '2015~'
]

plt.plot(years, kospi_avg_list)
plt.plot(years, gold_price_avg_list)
plt.legend(['kospi', 'gold'])
plt.show()



