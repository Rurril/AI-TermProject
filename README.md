# 주제 : Breaking CATPCHA!

### 목표 : `Text based captcha`를 뚫는 `Deep learning Model` 만들기

---

메인 파일 : [https://github.com/Rurril/AI-TermProject/blob/master/Captcha.ipynb]

사용해본 다른 모델 : `ResNet-50`, `VGG 16`, `LeNet-5`

![](https://github.com/Rurril/AI-TermProject/blob/master/images/8.png?raw=true)

위에 있는 사진이 최종 모델의 결과물

```python

model = Sequential()
# First convolutional layer with max pooling
model.add(Conv2D(32, (5, 5), padding="same", input_shape=(40, 40, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
# Second convolutional layer with max pooling
model.add(Conv2D(48, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
# Third convolutional layer with max pooling
model.add(Conv2D(64, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
# Hidden layer with 500 nodes
model.add(Flatten())
model.add(Dense(500, activation="relu"))
# Output layer with 32 nodes (one for each possible letter/number we predict)
model.add(Dense(62, activation="softmax"))
# Ask Keras to build the TensorFlow model behind the scenes
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.summary()

```

> 위의 코드가 가장 좋은 결과를 나타낸 모델

- Model Validation : 최대 약 90%
- Model Test : 모든 글자를 정확하게 판별한 경우 : 72.5%
- Model Test : 정확하게 판별한 것 중 옳바르게 판별한 경우 :  52.4%

---

[***직접 캡챠를 만들어보기 했지만***](https://github.com/Rurril/AI-TermProject/blob/master/captcha2.html) captcha 라이브러리가 강력해서 사용하였다.


`아래는 Captcha generator 코드를 작성하여 만든 결과물이다.`

![](https://github.com/Rurril/AI-TermProject/blob/master/images/5.png?raw=true)


`위의 캡챠 이미지들을 아래와 같이 문자 별로 나누어서 학습한다.`


![](https://github.com/Rurril/AI-TermProject/blob/master/images/6.png?raw=true)


학습하기 전에 grayscale로 바꾸는 등 많은 전처리 과정이 있지만 이 파일에서 설명은 생략하겠다. 

---

기존에 있던 논문들을 참고하진 않았고 처음 하는 DL 모델링이다보니 아는 지식 안에서 여러 모델들을 사용하였다. 좋은 결과라고는 확신을 할 수 없지만 교수님께서 꽤 좋은 결과를 낸 것 같다고 말씀해주셨다.

다만 피드백은, 한 generator로 학습했기 때문에 그 이미지 파일에 `overfitting` 된 것 같다고 말씀하시면서, 차라리 직접 만든 generator에서 뽑은 이미지도 학습했으면 좀 더 general한 모델이 됬을 거라고 말씀하셨다.




