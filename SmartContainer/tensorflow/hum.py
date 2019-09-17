import tensorflow as tf
import sys  # 종료를 위한 함수
import pandas as pd
import numpy as np

tf.set_random_seed(777)

learning_rate = 1e-7
data = pd.read_csv('dataset/item_hum.csv')
count = 5  # 품목 갯수에 따른 변화를 위한 변수

# csv파일로 관리
ice = data['ice'].values
apple = data['apple'].values
tuna = data['tuna'].values
pollack = data['pollack'].values
banana = data['banana'].values
pineapple = data['pineapple'].values
strawberry = data['strawberry'].values

x_data = [ice, apple, tuna, pollack, banana]  # 데이터 입력
y_data = [[95.], [80.], [70.], [80.], [75.]]  # 예상 데이터 값, 데이터베이스에서 끌어와야 함


# placeholders for a tensor that will be always fed.
# 여러번 호출을 위한 습도 AI함수 화
def humAI():
    X = tf.placeholder(tf.float32, shape=[None, 1000])  # N차원 모델의 개수를 5로 지정한 형태
    Y = tf.placeholder(tf.float32, shape=[None, 1])  # N차원 모델의 개수를 1로 지정한 형태


    W = tf.Variable(tf.random_normal([1000, 1]), name='weight')  # 가중치
    b = tf.Variable(tf.random_normal([1]), name='bias')  # 편향값

    # Hypothesis
    hypothesis = tf.matmul(X, W) + b  # Y = WX + b
    # Simplified cost/Loss function
    cost = tf.reduce_mean(tf.square(hypothesis - Y))

    # Minimize
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate) #cost를 최적화로 만드는 훈련
    train = optimizer.minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())  # 텐서 변수 초기화

    for step in range(310001):
        cost_val, hy_val, _ = sess.run(
            [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
        if step % 10000 == 0:
            print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

    hum = []
    for step in range(count):
        hum.append(np.round(hy_val[step]))
        print(hum[step])


'''
    #사용자가 지정한 값
    A = 5
    B = 12
    C = -20
    D = -15
    E = 20

    # 제어시 특정 온도보다 낮거나 높을 경우
    # 얼음 : A , 사과 : B,  참치 : C,  동태 : D,  바나나 : E 

    if(A > Temp[0] & A < Temp[0]):
        #재귀호출
        ALearn = AI() 
        print(Temp[0])
    if(B > Temp[1] & B < Temp[1]):
        #재귀호출
        BLearn = AI()
        print(Temp[1])
    if(C > Temp[2] & C < Temp[2]):
        #재귀호출
        CLearn = AI()
        print(Temp[2])
    if(D > Temp[3] & D < Temp[3]):
        #재귀호출
        DLearn = AI()
        print(Temp[3])
    if(E > Temp[4] & E < Temp[4]):
        #재귀호출
        ELearn = AI()
        print(Temp[4])
'''


# 추가에 대한 기계 학습, 인위적으로 넣어봄
def humAdd():
    global x_data
    global y_data
    global count
    add_item = int(input("추가하고자 하는 품목번호를 입력하세요. (1. 파인애플, 2. 딸기) "))
    if (add_item == 1):
        x_data += [pineapple]  # 추가된 항목의 데이터 셋을 넣어줌
        y_data += [[78.]]  # 예측값이 78일 때
        count = count + 1
        a3 = humAI()
        add = int(input('더 추가하시겠습니까? (1. 추가, 2. 종료) )'))
        if (add == 1):
            c = humAdd()
        elif (add == 2):
            sys.exit(1)

    elif (add_item == 2):
        x_data += [strawberry]  # 추가된 항목의 데이터 셋을 넣어줌
        y_data += [[82.]]  # 예측값이 82일 때
        count = count + 1
        a4 = humAI()
        add = int(input('더 추가하시겠습니까? (1. 추가, 2. 종료) )'))
        if (add == 1):
            c = humAdd()
        elif (add == 2):
            sys.exit(1)
    else:
        print('값을 찾을 수 없습니다.')
        a5 = humAdd()


a1 = humAI()

menu = int(input('1. 추가  2. 종료 '))
if (menu == 1):
    a2 = humAdd()
elif (menu == 2):
    print('이용해주셔서 감사합니다.')
    sys.exit(1)













