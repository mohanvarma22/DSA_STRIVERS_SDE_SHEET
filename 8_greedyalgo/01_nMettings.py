#sort using the end point and posn
def maxMeetings(s,e,n):
    meet = [(s[i],e[i],i+1) for i in range(n)]
    sorted(meet,key=lambda x:(x[1],x[2]))
    answer = []
    limit = meet[0][1]
    answer.append(meet[0][2])
    for i in range(1,n):
        if meet[i][0] > limit:
            limit = meet[i][1]
            answer.append(meet[i][2])
    for pos in answer:
        print(pos, end=" ")

s = [1, 3, 0, 5, 8, 5]
e = [2, 4, 6, 7, 9, 9]
n = len(s)
maxMeetings(s, e, n)