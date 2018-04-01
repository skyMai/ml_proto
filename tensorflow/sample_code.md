---
title: tensorflow sample code
tags: tensorflow
notebook: deeplearning.ai
---

### 1. Basic sample

*Exercise*: 

```python
input_x = np.array([[1.0],[-20.],[100.]])

w = tf.Variable(0,dtype = tf.float32)
x = tf.placeholder(tf.float32, [3,1])

#cost=tf.add(tf.add(w**2,tf.multiply(-10.,w)),25)
#cost = w**2 - 10*w + 25
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
for i in range(1000):
    session.run(train, feed_dict={x:input_x})
print(session.run(w))

```

