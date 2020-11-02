# Hanium_IoT_SmartContainer

2019 한이음 해상물류
[19-P632] 항만 물류를 최적화 해주는 스마트 컨테이너

#### 시연 영상
  - YOUTUBE: https://www.youtube.com/watch?v=9Vx05kWheak

#### 목적
> 해상 물류의 운송 수단인 컨테이너에 내부 환경에 대한 제어와 외부를 감시할 수 있는 장치를 부착하여 
 원격 환경에서 컨테이너 내부의 온/습도를 제어하고 컨테이너의 고장을 감지하는데 목적이 있음.

#### 사용 언어 및 환경
웹 front 및 back 개발
- Windows10
- Python3.7
- Javascript
- redis

하드웨어 개발
- Ubuntu 16.04
- nodeMcu, Esp-32
- C++

### 기능 흐름도
![컨테이너 흐름도](https://user-images.githubusercontent.com/44918187/97858836-165add00-1d43-11eb-9302-060f56f36317.jpg)

1. Module과 Server가 Socket 연결을 수립하여 제어가능한 상태가 되도록 함
2. 기존에 설정된 값 또는 새로운 설정 값으로 각 모듈을 제어

### 문제점 및 해결방안
- 프로젝트 관리 측면   
	- git에 관한 문제점.   
		- 팀원들 모두가 git에 익숙하지 않아 pull commit push 과정에서 여러 conflict가 발생하여 이를 해결하기 위해 다같이 git을 공부하고 오류를 최소화하기 위해 같은 코드를 여러명이서 편집하지 않고 분할하여 코딩하고 commit하는 방식으로 해결하였음.
    - ​프로젝트 일정에 관한 문제점
      	- 미리 설계한 개발일정 보다 실제 개발 진행도가 많이 늦어지는 경향이 있어 팀원들이 서로 분담한 역할 외에 서로의 영역을 도와주는 방식으로 해결하였음.
    - ​협업에 관한 문제점
    	- 팀원 서로 코드를 작성하는 스타일이 다르고 어떤 함수가 무엇을 의미하는지 파악 할 수 없어서 네이밍 규칙을 정하고 주석을 통해 직관적으로 알 수 있게 하였음.
- 작품 개발 측면
	 - ​Nodemcu에서 잘 작동하던 Websocket 라이브러리가 ESP32에서 정상적으로 작동하지 않던 오류.  
	 	- nodemcu에서 정상적으로 작동하던 Websocket라이브러리가 ESP32에. 적용하자 컴파일이. 이루어지지 않아 소켓 서버에 접속하지 못해 이를 해결하기위해 log에 찍힌 에러메시지를 라이브러리 제작자 github에 질문하고, stackoverflow에서 검색도 해보았지만 별다른 결과를 얻지못해 직접 해결하기로 마음먹고 문제가 발생한 헤더의 몇 번째 라인인지 찾아 코드를 수정하고 적용해보았지만 다른 헤더가 오류를 발생하는 식으로 문제가 커져서 오류가 발생한 헤더 파일을 모두 찾아서 버그를 수정하고 컴파일하여 해결한 경험이 있음
    - ​​Socket 그룹 생성
    	- python의 web framework인 django 라이브러리 django-channels를 이용하여 소켓 그룹을 형성하여 제어 주체가 보낸메시지를 모든 모듈이 수신하고 이를 통해 전체적인 제어를 하려고 하였음 , 이를 위해 stackoverflow와 channels 공식 문서를 살펴보며 그룹을 생성하는 코드와 이 그룹에 특정 제어 메시지를 보내는 방법을 찾아 해결하였음.
    - ​​온도 하강 모듈의 Relay와 연결된 전선이 녹아버린 경우
    	- 온도하강 모듈의 Relay와 배터리가 연결된 부분의 플라스틱과 전선이 녹아버려 문제점이 무엇인지 확인하기위해 릴레이 교체를 하였으나 또다시 같은 문제가 발생하여 전선의 품질에 문제가 있다고 판단하여 더 두껍고 좋은 전선으로 교체하여 해결 하였음.


### 수상 및 창업
- 삼육대학교 프로젝트 경진대회 대상.
- 스마트 항만물류 창업지원 사업(동기부여 패키지) 선정.
![image](https://user-images.githubusercontent.com/44918187/89751512-642cc400-db0b-11ea-8ecb-ff97bceeedc5.png)
