class Perceptron(object):
    def __init__(self, input_data, output_size):
        self.X = input_data # input_Data == tf.placeholder([Batch,Size])

        # check data type
        if len(input_data.shape) != 2:
            raise ValueError("Wrong input data shape - " + self.__class__.__name__)

        input_size = input_data.shape[-1]
        # block 1
        self.W1 = tf.Variable(tf.zeros([input_size, output_size]))
        self.b1 = tf.Variable(tf.zeros([output_size]))

        self.output = tf.matmul(self.X, self.W1) + self.b1

class Feedforward(object):
    def __init__(self, input_data, output_size, hidden_layers_size):
        self.X = input_data # input_Data == tf.placeholder([Batch,Size])

        if len(input_data.shape) != 2:
            raise ValueError("Wrong input data shape - " + self.__class__.__name__)
        if type([]) != type(hidden_layer_size):
            raise ValueError("Wrong hidden_layer_size - " + self.__class__.__name__)

        input_size = input_data.shape[-1]
        # blocks
        self.Ws = []
        self.bs = []
        loop = [input_size] + hidden_layer_size + [output_size]
        for i in range(len(loop) - 1):
            Ws.append(tf.Variable(tf.zeros([loop[i], loop[i+1]])))
            bs.append(tf.Variable(tf.zeros(loop[i+1])))

        self.output = self.X
        for i in range(len(Ws)):
            self.output = tf.matmul(self.output, Ws[i]) + self.bs[i]
