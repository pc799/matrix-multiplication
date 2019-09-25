"""
Program type: Python 3.6.5
Program name: Stassen's matrix multiplication.
Sub. Date   : 16-03-2019
"""
import random as r
"""
#Exception RuntimeError: 'maximum recursion depth exceeded'
import sys
sys.setrecursionlimit(10000)
"""
#Method to split the matrix into four parts
def splitMat(A):
  length = len(A)
  mid = length // 2

  #topleft
  top_left = [[0 for j in range(mid)] for i in range(mid)]
  for i in range(mid):
    for j in range(mid):
      top_left[i][j] = A[i][j]

  #botleft
  bot_left = [[0 for j in range(mid)] for i in range(mid, length)]
  n = len(bot_left)
  for i,x in zip(range(mid, length), range(n)):
    for j,y in zip(range(mid), range(n)):
      bot_left[x][y] = A[i][j]

  #topright
  top_right = [[0 for j in range(mid, length)] for i in range(mid)]
  n = len(top_right)
  for i,x in zip(range(mid), range(n)):
    for j,y in zip(range(mid, length), range(n)):
      top_right[x][y] = A[i][j]

  #botright
  bot_right = [[0 for j in range(mid, length)] for i in range(mid, length)]
  n = len(bot_right)
  for i,x in zip(range(mid, length), range(n)):
    for j,y in zip(range(mid, length), range(n)):
      bot_right[x][y] = A[i][j]

  return top_left, top_right, bot_left, bot_right

#Method to add two matrix
def add(A, B):
  n = len(A)
  C = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] + B[i][j]
  return C

#Method to subtract two matrix
def sub(A, B):
  n = len(A)
  C = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      C[i][j] = A[i][j] - B[i][j]
  return C

#Trivial matrix multiplication
def mul(A, B):
  n = len(A)
  C = [[0 for j in range(n)] for i in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]
  return C

#Strassen's matrix multiplication
def multiply(matA, matB):
  if (len(matA), len(matA[0])) == (2, 2):
    return mul(matA, matB)

  A, B, C, D = splitMat(matA)
  E, F, G, H = splitMat(matB)

  p1 = multiply(A, sub(F, H))
  p2 = multiply(add(A, B), H)
  p3 = multiply(add(C, D), E)
  p4 = multiply(D, sub(G, E))
  p5 = multiply(add(A, D), add(E, H))
  p6 = multiply(sub(B, D), add(G, H))
  p7 = multiply(sub(A, C), add(E, F))

  top_left = add(sub(add(p5, p4), p2), p6)
  top_right = add(p1, p2)
  bot_left = add(p3, p4)
  bot_right = sub(sub(add(p1, p5), p3), p7)
  
  #Joining the results together into single matrix
  newMat = []
  for i in range(len(top_right)):
      newMat.append(top_left[i] + top_right[i])
  for i in range(len(bot_right)):
      newMat.append(bot_left[i] + bot_right[i])
  return newMat

"""
Program main section
Input : size of the matrices in exponent of 2's.
Output: Resulatant matrix obtained through multiplication
"""
size = int(input('Enter the size[2^]:'))
mat1 = [[r.randrange(100) for j in range(size)] for i in range(size)]
mat2 = [[r.randrange(100) for j in range(size)] for i in range(size)]
print('A:' + str(mat1))
print('B:' + str(mat2))
res = multiply(mat1, mat2)
print('Result:' + str(res))
"""
#For testing:
rep = mul(mat1, mat2)
print('Test  :' + str(rep))
"""
"""
References: 
https://en.wikipedia.org/wiki/Strassen_algorithm
https://www.geeksforgeeks.org/strassens-matrix-multiplication/
http://oucsace.cs.ohiou.edu/~razvan/courses/cs4040/lecture12.pdf
https://www.coursera.org/specializations/algorithms
CME 323:  Distributed Algorithms and Optimization, Spring 2016. Lecture 3, 04/04/2016.
Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. Introduction to Algorithms.

email: imfclaws@gmail.com
end_of_the_program.
"""
