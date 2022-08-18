<Description>
  주류에 대한 정보와 추천서비스를 제공하는 웹사이트로서 다양한 정보 공유 및 커뮤니티 활동이 가능합니다. 	

<Environment>
 OS : Windows 10 x64
 python==3.8
 django==2.2.5

<Prerequisite>
 sklearn v0.24.1 머신러닝 분석관련 라이브러리
 lightgbm v3.1.1 학습모델 관련 라이브러리
 pillow v8.2.0 이미지 관리 라이브러리
 bcrypt v3.2.0 암호화 라이브러리
 pyjwt v1.7.1 복호화 라이브러리
 numpy v1.20.1 데이터 연산 라이브러리 
 pandas v1.2.4 데이터 연산 라이브러리

<Files>
 crawling : 데이터 크롤링시 사용한 소스코드가 들어있는 폴더
 etc : 머신러닝 관련 소스코드가 들어있는 폴더
 server : 웹페이지 관련 소스코드가 들어있는 폴더