import numpy

string = input()
s = string.split(" ")
N = int(s[0])
M = int(s[1])
arr = numpy.zeros(shape=(N,M),dtype=int)


for i in range (N):
    string = input()
    s = string.split(" ")
    for j in range (M):
        arr[i,j] = int(s[j])
print(arr.transpose())
print(arr.flatten())
