#모자 문제 
#나는 야구장 입장 알바다. 야구장에는 모자를 한 방향으로만 착용하고 입장을 해야한다는 조건이있다.
#단 한번만 주문을 해 입장객들의 모자 방향을 한 방향으로 통일시키려면 어떻게 해야할까?
# F = "앞방향" B = "뒷방향"



from ast import Try


cap1 = ["F","F","B","B","B","F","B","B","B","F","F","B","F"]

cap2 = ["F","F","B","B","B","F","B","B","B","F","F","F","F"]

cap3 = ["F","F","B","H","B","F","B","B","B","F","H","F","F"]



def pleaseConformOnepass(caps):
    
    if caps != []:
        caps = caps + [caps[0]]
    else:
        print("오늘은 휴무입니다.")
    start = []
    end = []
    
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                start.append(i)
                print(start)
            else:
                end.append(i-1)
                print(end,"엔드")
 
    for j in range(len(start)):
        if start[j]!=end[j]:
            print(f"People in positions {start[j]} through {end[j]} flip your caps!")
        else:
            print(f"Person at position {start[j]} flip your cap!")

    

pleaseConformOnepass(cap3)

# def pleaseConform(caps):
#     start = forword = backword = 0
#     itervals = []
#     caps = caps + ["END"]
#     for i in range(1,len(caps)):
#         if caps[start] != caps[i]: # true일 경우 한개 구간을 종료시키고 현재 i로부터 새로운 구간을 시작, 리스트 요소 F가 다음 요소와 안맞을 때 
#             itervals.append((start,i-1,caps[start])) #첫번째 튜플 시작지점, 두번째 끝 지점, 세번째 모자방향
#             if caps[start] == "F":
#                 forword +=1
#             else:
#                 backword += 1
#             start = i
#     if forword < backword:
#         flip ="F"
#     else: 
#         flip = "B"
#     for t in itervals:
#         #여기서 t는 앞서 저장한 튜플
#         if t[2] == flip:
#             print("people in position",t[0],"through",t[1],"flip your caps!")         
#             print(t[0])         
#             print(t[1])         

   
# pleaseConform(cap2) 

