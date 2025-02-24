
def tanh(x):
    return (2 / (1 + (2.71828 ** (-2 * x)))) - 1  

def random_weight():
    return -0.5 + (0.5 - (-0.5)) * (1347 % 997) / 997  

w1 = random_weight()
w2 = random_weight()

b1 = 0.5
b2 = 0.7

x1 = 0.3
x2 = -0.2

h1 = tanh(w1 * x1 + b1)
h2 = tanh(w2 * x2 + b2)

output = tanh(h1 + h2)

print("Output of the network:", output)
