print 'Content-Type: text/plain'
print ''

print 'Hello, World!'
print ''

# -------------------------
# Fibonacci Sequence
# -------------------------
print 'Fibonacci Sequence (first 10 terms):'

a = 0
b = 1
for i in range(10):
    print a
    a, b = b, a + b

print ''

# -------------------------
# Factorial Sequence
# -------------------------
print 'Factorial Sequence (1 to 5):'

fact = 1
for i in range(1, 6):
    fact = fact * i
    print 'Factorial of', i, '=', fact

print ''

# -------------------------
# Table of 5
# -------------------------
print 'Table of 5:'

for i in range(1, 11):
    print '5 x', i, '=', 5 * i
