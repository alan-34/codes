print 'Content-Type: text/plain'
print ''

print '============================================'
print '          WELCOME TO THE PRACTICE APP        '
print '============================================'
print ''

# --------------------------------------------------
# ASSIGNMENT 1: Fibonacci Series (First 10 Elements)
# --------------------------------------------------
print '--- Fibonacci Series ---'
a = 0
b = 1
for i in range(10):
    print a
    a, b = b, a + b

print ''  # Creates a blank line spacing

# --------------------------------------------------
# ASSIGNMENT 2: Student Details (5 Times)
# --------------------------------------------------
print '--- Student Details ---'
name = "Your Name"
seat_no = "12345"
dept = "Computer Engineering"

for i in range(5):
    print 'Name:', name, ' | Seat Number:', seat_no, ' | Department:', dept

print ''  # Creates a blank line spacing

# --------------------------------------------------
# ASSIGNMENT 3: Table of 10
# --------------------------------------------------
print '--- Table of 10 ---'
for i in range(1, 11):
    print '10 x', i, '=', 10 * i