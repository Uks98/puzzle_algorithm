
# 파티에 참석하기 좋은시간
#한시간이 주어졌을 때 가장많은 연예인을 만날 수 있는 시간대를 구하기

#튜플0번 = 연예인 도착 시간 , 튜플1번 연예인이 떠나는 시간


# sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
#          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]

# def bestTime(schedule):
#     times = [] #시작시간과 끝시간이 담긴다.
#     for c in schedule:
#         times.append((sched2[0],"start"))
#         times.append((sched2[1],"end"))
#     sortList(times)
#     maxcount,time = chooseTime(times)
#     print('Best time to attend the party is at', time, 'o\' clock : ', maxcount, 
#           'celebrities will be attending!')

# def sortList(tlist):
#     for ind in range(len(tlist)-1):
#         ism = ind
#         for i in range(ind,len(tlist)):
#             if tlist[ism][0]>tlist[i][0]:
#                 ism = i
#             tlist[ind],tlist[ism] = tlist[ism],tlist[ind]

# def chooseTime(times):
#     rcount = 0
#     maxcount = time = 0
#     for t in times:
#         if t[1] == 'start':
#             rcount = rcount + 1
#         elif t[1] == 'end':
#             rcount = rcount -1
#         if rcount > maxcount:
#             maxcount = rcount
#             time = t[0]
#     return maxcount, time


# bestTime(sched2)