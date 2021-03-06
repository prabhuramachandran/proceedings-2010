import numpy
import theano.tensor as T
from theano import shared, function
rng = numpy.random

# Declare Theano variables
x = T.matrix()
y = T.vector()
w = shared(rng.randn(100))
b = shared(numpy.zeros(()))
print "Initial model:"
print w.value, b.value

# Construct Theano expression graph
p_1 = 1 / (1 + T.exp(-T.dot(x, w)-b))
xent = -y*T.log(p_1) - (1-y)*T.log(1-p_1)
prediction = p_1 > 0.5
cost = xent.mean() + 0.01*(w**2).sum()
gw,gb = T.grad(cost, [w,b])

# Compile expressions to functions
train = function(
            inputs=[x,y],
            outputs=[prediction, xent],
            updates={w:w-0.1*gw, b:b-0.1*gb})
predict = function(inputs=[x], outputs=prediction)

N = 4
feats = 100
D = (rng.randn(N, feats), rng.randint(size=4,low=0, high=2))
training_steps = 10
for i in range(training_steps):
    pred, err = train(D[0], D[1])
print "Final model:"
print w.value, b.value

print "target values for D"
print D[1]

print "prediction on D"
print predict(D[0])
