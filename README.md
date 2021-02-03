# Momentum Project

## 1. Momentum 최적화 알고리즘의 개요 및 동작원리

<img width="416" alt="모멘텀" src="https://user-images.githubusercontent.com/28584213/106716361-b1649b00-6641-11eb-8d2c-0462905f11cf.png">


## 2. Tensorflow로 구현한 Momentum 동작 코드와 단위 테스트 코드

#### testTM\_#1.py 실행 결과

![testTM_#1](https://user-images.githubusercontent.com/28584213/106716502-de18b280-6641-11eb-92f0-02ffbe34c432.png)

#### testTM_#2.py 실행 결과

![testTM_#2-1](https://user-images.githubusercontent.com/28584213/106716547-ebce3800-6641-11eb-9fe9-4a8db05aae1a.png)

![testTM_#2-2](https://user-images.githubusercontent.com/28584213/106716553-ee309200-6641-11eb-8fbc-5a66295906f0.png)


#### Source Code

* tensorflow_momentum.py
* testTM\_#1.py
* testTM\_#2.py



## 3. Momentum 알고리즘의 구체화


#### Source Code

* momentum.py


## 4. Momentum과 GD(경사하강법) 구체화 모듈의 단위 테스트 작업

#### testM.py 실행 결과

![testM](https://user-images.githubusercontent.com/28584213/106716732-20da8a80-6642-11eb-9de4-bf89cdb8abed.png)


#### Source Code

* testM.py


## 5. Momentum 알고리즘 성능 검증

* 로젠브룩 함수를 이용해 두 알고리즘의 결과를 비교함으로써 성능을 검증


#### checkMomentum\_#1.py

![checkMomentum_#1-2](https://user-images.githubusercontent.com/28584213/106716964-65febc80-6642-11eb-9041-9c2008a6aeda.png)

![checkMomentum_#1-1](https://user-images.githubusercontent.com/28584213/106716961-65662600-6642-11eb-8865-96b33a7de005.png)



#### checkMomentum\_#2.py

![checkMomentum_#2-2](https://user-images.githubusercontent.com/28584213/106717017-76169c00-6642-11eb-8432-dd57f034122e.png)

![checkMomentum_#2-1](https://user-images.githubusercontent.com/28584213/106717023-7747c900-6642-11eb-87c6-d29f464a11af.png)


#### Source Code

* checkMomentum\_#1.py
* checkMomentum\_#2.py
