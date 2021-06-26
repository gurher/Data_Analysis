# 1. 주제 : "KOSPI와 금가격"

지난 30년간 코스피와 금 가격 추이를 통한 비교
금융위기 당시 변동률 비교분석을 통한 안전성 분석

<br>

# 2. 데이터
### 데이터 출저

https://www.kaggle.com/zerojay0311/kospi-dataset-since-199001202011

<br>

https://www.kaggle.com/shikhnu/gold-price

# 3. 테이블 생성과 데이터 로드

create table kospi

(num varchar(20), 

date varchar(20), 

value varchar(20), 

diff varchar(20), 

fluctuation varchar(20), 

volume varchar(20), 

tradingvalue varchar(20) );

 

LOAD DATA LOCAL INFILE '/home/scott/kospi.csv'

REPLACE

INTO TABLE kospi

fields TERMINATED BY ','

ENCLOSED BY '"'

LINES TERMINATED BY ‘\n’;


![image](https://user-images.githubusercontent.com/78076900/123503662-5cc4c980-d68f-11eb-9be3-c67d438d3f90.png)

<br>

![image](https://user-images.githubusercontent.com/78076900/123503667-64846e00-d68f-11eb-94c2-2040968075fd.png)

# 4. 데이터 시각화 

## 1)1990~2020 kospi 와 국제금값 그래프


![image](https://user-images.githubusercontent.com/78076900/123503705-9269b280-d68f-11eb-955e-d7128098f8d5.png)

코스피,금값 모두 기준점 시초가 대비 3~4배가량 상승하였습니다.

구간별 등락을 반복하며 전체적으로 우상향 그래프를 그리고 있습니다.

## 2) 97년 외환위기

![image](https://user-images.githubusercontent.com/78076900/123503726-aca39080-d68f-11eb-998c-7c845eff53ae.png)

97년 외환위기 구간에서 코스피의 40% 정도의 가파른 하락을 그래프로 확인할 수 있습니다. 이에 비해 금가격은 변동성이 적은 그래프모양을 보입니다.

## 3) 2007 금융위기

![image](https://user-images.githubusercontent.com/78076900/123503741-c2b15100-d68f-11eb-8914-0312d33bd046.png)


리먼브라더스발 금융 위기로 인해 2007년부터 2009년 까지 코스피가 급격히 하락하다가 반등하는 그래프를 보입니다.

이에 비해 금값은 500대에서 1200대까지 두배이상의 성장세를 보입니다.


# 5. 결론

코스피와 국제금가격은 지난 30년간 등락을 반복하며 우상향하고 있는 것을 그래프를 통해 확인했습니다. 
97년 외환위기와 2008년 금융위기 당시 코스피는 큰 폭으로 하락한데반해 금가격은 상대적으로 안전성을 보여주었습니다.

최근 코스피는 3000을 넘어 장기적으로 지수가 우상향할 것 이라고 예상되지만 단기적으로 등락을 반복하면 조정될 가능성이 있습니다. 
이에 따라 대표적인 안전자산인 금에 분산 투자를 통해 금융위기 시 효율적인 리스크 관리를 할 수 있을 것으로 판단됩니다.
