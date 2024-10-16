import tensorflow as tf

class SReLU(tf.keras.layers.Layer):
    def __init__(self, alpha=1.0, beta=0.1):
        super(SReLU, self).__init__()
        self.alpha = alpha
        self.beta = beta

    def call(self, inputs):
        pos = tf.maximum(0.0, inputs) * self.alpha
        neg = self.beta * (tf.exp(tf.minimum(0.0, inputs)) - 1.0)
        return pos + neg
