import csv#output list to csv
def compute_jaccard(list_1, list_2):#compute jaccard similarity
    sim = 0
    for x in range(16):
        if list_1[x]==list_2[x] and list_1[x] != 'N':
            sim += 1
    return sim/16.0
file = open("test.txt", 'r')
a = 0
list = []
#read testdata into list
while True:
    line = file.readline()
    if not line: break
    line = line.rstrip()
    list.append(line.split(","))
    a += 1
file.close()
s1 = []
s2 = []
#start clustering, get the biggest cluster according to statistics
for x in range(a):
    if list[x][3]== '0' or list[x][3]== 'N':
        s1.append(x)
    else:
        s2.append(x)
a = len(s2)
b = len(s1)
board = []
#add more similar data to cluster1
for x in range(a):
    score = 0
    for y in range(b):
        plus = compute_jaccard(list[s1[y]], list[s2[x]])
        score += plus
    board.append((score, s2[x]))
board.sort()
board.reverse()
for x in range(5):
    s1.append(board[x][1])
    s2.remove(board[x][1])
s1.sort()
#adjust to real ID
for x in range(len(s1)):
    s1[x] += 1
for x in range(len(s2)):
    s2[x] += 1
#output csv files
out = open("cluster1.csv", 'wb')
thecsv = csv.writer(out)
for value in s1:
    thecsv.writerow([value])
out.close()
out = open("cluster2.csv", 'wb')
thecsv = csv.writer(out)
for value in s2:
    thecsv.writerow([value])
out.close()

