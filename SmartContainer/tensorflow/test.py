import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
import datetime

data = pd.read_csv('dataset/ulsan001.csv')
# data.head()

if(int(input('데이터를 추가 하시겠습니까? (yes : 1, no : 0) ')) == 1):
    number1 = input('목재 값을 입력하세요: ')
    number2 = input('가스 값을 입력하세요: ')
    number3 = input('의류 값을 입력하세요: ')
    number4 = input('원석 값을 입력하세요: ')

    #넣을 데이터
    new_df = pd.DataFrame([{'wood': number1, 'gas': number2, 'cloth': number3, 'gemstone': number4}])
    #넣은 데이터와 기존 데이터의 결합
    final_df = pd.concat([data, new_df])
    #새로운 파일로 CSV 파일로 저장
    final_df.to_csv('dataset/ulsan001.csv', index=False)

    new_data = pd.read_csv('dataset/ulsan001.csv')

    wood = new_data['wood'].values
    gas = new_data['gas'].values
    cloth = new_data['cloth'].values
    gemstone = new_data['gemstone'].values
else:
    wood = data['wood'].values
    gas = data['gas'].values
    cloth = data['cloth'].values
    gemstone = data['gemstone'].values

# 50개의 열 = 윈도우
seq_len = 50
sequence_length = seq_len + 1 #예측 한개

def fig1():
    result1 = []

    for index in range(len(wood) - sequence_length):
        result1.append(wood[index: index + sequence_length])

    normalized_data1 = []

    # 정규화
    for window in result1:
        normalized_window1 = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data1.append(normalized_window1)

    result1 = np.array(normalized_data1)

    # train 과 test 를 나눔
    row1 = int(round(result1.shape[0] * 0.9)) #90퍼센트는 train 10%는 test
    train1 = result1[:row1, :]
    np.random.shuffle(train1) # 셔플해줘야 결과값이 잘나옴

    x_train1 = train1[:, :-1]  # X에 50개
    x_train1 = np.reshape(x_train1, (x_train1.shape[0], x_train1.shape[1], 1))
    y_train1 = train1[:, -1]  # Y에 1개

    x_test1 = result1[row1:, :-1]  # X에 50개
    x_test1 = np.reshape(x_test1, (x_test1.shape[0], x_test1.shape[1], 1))
    y_test1 = result1[row1:, -1]  # Y에 1개

    # 케라스 함수를 불러옴
    model = Sequential()
    # AI중 LSTM기법 사용
    model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(LSTM(62, return_sequences=False))

    model.add(Dense(1, activation='linear'))

    model.compile(loss='mse', optimizer='rmsprop')

    model.summary()
    # AI에 데이터를 넣고 학습시킴 , batchsize는 한번에 몇개를 학습시키냐를 의미하고 epochs는 몇번 학습시킬지를 나타냄
    model.fit(x_train1, y_train1,
              validation_data=(x_test1, y_test1),
              batch_size=30,
              epochs=100)

    pred1 = model.predict(x_test1)

    fig = plt.figure(facecolor='white', figsize=(20, 10))
    ax = fig.add_subplot(111)
    plt.title('wood graph')
    ax.plot(y_test1, label='real_wood')
    ax.plot(pred1, label='prediction_wood')

    ax.legend()
    plt.show()

    fig.savefig(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test1.png', format='png')

def fig2():
    result2 = []

    for index in range(len(gas) - sequence_length):
        result2.append(gas[index: index + sequence_length])

    normalized_data2 = []

    for window in result2:
        normalized_window2 = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data2.append(normalized_window2)

    result2 = np.array(normalized_data2)

    row2 = int(round(result2.shape[0] * 0.9))
    train2 = result2[:row2, :]
    np.random.shuffle(train2)

    x_train2 = train2[:, :-1]  # X에 50개
    x_train2 = np.reshape(x_train2, (x_train2.shape[0], x_train2.shape[1], 1))
    y_train2 = train2[:, -1]  # Y에 1개

    x_test2 = result2[row2:, :-1]  # X에 50개
    x_test2 = np.reshape(x_test2, (x_test2.shape[0], x_test2.shape[1], 1))
    y_test2 = result2[row2:, -1]  # Y에 1개

    # 케라스 함수를 불러옴
    model = Sequential()
    # AI중 LSTM기법 사용
    model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(LSTM(62, return_sequences=False))

    model.add(Dense(1, activation='linear'))

    model.compile(loss='mse', optimizer='rmsprop')

    model.summary()

    model.fit(x_train2, y_train2,
              validation_data=(x_test2, y_test2),
              batch_size=30,
              epochs=100)

    pred2 = model.predict(x_test2)

    fig = plt.figure(facecolor='white', figsize=(20, 10))
    ax = fig.add_subplot(111)

    plt.title('gas graph')
    ax.plot(y_test2, label='real_gas')
    ax.plot(pred2, label='prediction_gas')

    ax.legend()
    plt.show()

    fig.savefig(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test2.png', format='png')

def fig3():
    result3 = []

    for index in range(len(cloth) - sequence_length):
        result3.append(cloth[index: index + sequence_length])

    normalized_data3 = []

    for window in result3:
        normalized_window3 = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data3.append(normalized_window3)

    for window in result3:
        normalized_window3 = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data3.append(normalized_window3)

    result3 = np.array(normalized_data3)

    row3 = int(round(result3.shape[0] * 0.9))
    train3 = result3[:row3, :]
    np.random.shuffle(train3)

    x_train3 = train3[:, :-1]  # X에 50개
    x_train3 = np.reshape(x_train3, (x_train3.shape[0], x_train3.shape[1], 1))
    y_train3 = train3[:, -1]  # Y에 1개

    x_test3 = result3[row3:, :-1]  # X에 50개
    x_test3 = np.reshape(x_test3, (x_test3.shape[0], x_test3.shape[1], 1))
    y_test3 = result3[row3:, -1]  # Y에 1개

    # 케라스 함수를 불러옴
    model = Sequential()
    # AI중 LSTM기법 사용
    model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(LSTM(62, return_sequences=False))

    model.add(Dense(1, activation='linear'))

    model.compile(loss='mse', optimizer='rmsprop')

    model.summary()
    # AI에 데이터를 넣고 학습시킴 , batchsize는 한번에 몇개를 학습시키냐를 의미하고 epochs는 몇번 학습시킬지를 나타냄
    model.fit(x_train3, y_train3,
              validation_data=(x_test3, y_test3),
              batch_size=30,
              epochs=100)

    pred3 = model.predict(x_test3)

    fig = plt.figure(facecolor='white', figsize=(20, 10))
    ax = fig.add_subplot(111)

    plt.title('cloth graph')
    ax.plot(y_test3, label='real_cloth')
    ax.plot(pred3, label='prediction_cloth')

    ax.legend()
    plt.show()

    fig.savefig(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test3.png', format='png')

def fig4():
    result4 = []

    for index in range(len(gemstone) - sequence_length):
        result4.append(gemstone[index: index + sequence_length])

    normalized_data4 = []

    for window in result4:
        normalized_window4 = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data4.append(normalized_window4)

    result4 = np.array(normalized_data4)

    row4 = int(round(result4.shape[0] * 0.9))
    train4 = result4[:row4, :]
    np.random.shuffle(train4)

    x_train4 = train4[:, :-1]  # X에 50개
    x_train4 = np.reshape(x_train4, (x_train4.shape[0], x_train4.shape[1], 1))
    y_train4 = train4[:, -1]  # Y에 1개

    x_test4 = result4[row4:, :-1]  # X에 50개
    x_test4 = np.reshape(x_test4, (x_test4.shape[0], x_test4.shape[1], 1))
    y_test4 = result4[row4:, -1]  # Y에 1개

    # 케라스 함수를 불러옴
    model = Sequential()
    # AI중 LSTM기법 사용
    model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(LSTM(62, return_sequences=False))

    model.add(Dense(1, activation='linear'))

    model.compile(loss='mse', optimizer='rmsprop')

    model.summary()
    # AI에 데이터를 넣고 학습시킴 , batchsize는 한번에 몇개를 학습시키냐를 의미하고 epochs는 몇번 학습시킬지를 나타냄
    model.fit(x_train4, y_train4,
              validation_data=(x_test4, y_test4),
              batch_size=30,
              epochs=100)

    pred4 = model.predict(x_test4)

    fig = plt.figure(facecolor='white', figsize=(20, 10))
    ax = fig.add_subplot(111)

    plt.title('gemstone graph')
    ax.plot(y_test4, label='real_gemstone')
    ax.plot(pred4, label='prediction_gemstone')

    ax.legend()
    plt.show()

    fig.savefig(r'C:\Users\han\Desktop\SmartContainer\SmartContainer\Container\images\test4.png', format='png')

graph = int(input('1. 목재 2. 가스  3. 의류 4. 원석'))

if(graph == 1):
    a = fig1()
if(graph == 2):
    b = fig2()
if(graph == 3):
    c = fig3()
if(graph == 4):
    d = fig4()