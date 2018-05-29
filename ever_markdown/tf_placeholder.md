---
title: tensorflow:placeholder vs. Variable
tags: tensorflow
notebook: deep learning&machine learning
---

### placeholder和Variable的区别？

> 二者的主要区别在于：

- tf.Variable：主要在于一些可训练变量（trainable variables），比如模型的权重（weights，W）或者偏置值（bias）

    - 声明时，`必须提供初始值`；
    - 名称的真实含义，在于变量，也即在真实训练时，其值是会改变的，自然事先需要指定初始值；
    
```python 
weights = tf.Variable(
    tf.truncated_normal([IMAGE_PIXELS, hidden1_units],
            stddev=1./math.sqrt(float(IMAGE_PIXELS)), name='weights')
)
biases = tf.Variable(tf.zeros([hidden1_units]), name='biases')
```

- tf.placeholder：用于得到传递进来的真实的训练样本：

    - 不必指定初始值，可在运行时，通过 Session.run 的函数的 feed_dict 参数指定,存放输入样本的
    - 这也是其命名的原因所在，仅仅作为一种占位符；

```python
images_placeholder = tf.placeholder(tf.float32, shape=[batch_size, IMAGE_PIXELS])
labels_placeholder = tf.placeholder(tf.int32, shape=[batch_size])
```

如下则是二者真实的使用场景：
```python
for step in range(FLAGS.max_steps):
    feed_dict = {
        images_placeholder = images_feed,
        labels_placeholder = labels_feed
    }
    _, loss_value = sess.run([train_op, loss], feed_dict=feed_dict)
```
当执行这些操作时，tf.Variable 的值将会改变，也即被修改，这也是其名称的来源（variable，变量）。