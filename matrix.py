a = [[3,4],[9,8]]
b = [[7,2],[0,1]]
r = [[0,0],[0,0]]

# a[0] [0] ==> 3
# b[0] [0] ==> 7
# First element
# a [0] [0] + b [0][0] ==> 10

r[0][0] = a[0][0] + b[0][0]
r[0][1] = a[0][1] + b[0][1]
r[1][0] = a[1][0] + b[1][0]
r[1][1] = a[1][1] + b[1][1]

print(r)