
name = 'ruslan'
if len(name) < 100:
    list2 = []
    for alpha in name:
        if alpha not in list2:
            list2.append(alpha)
    if len(list2) % 2 == 0:
        print('CHAT WITH HER')
    else:
        print('ignor')


n = int(input('кол-во учеников: '))
h = int(input("высота забора: "))
list1 = []
for i in range(n):
    rost = int(input())
    list1.append(rost)
lat = 0
for j in list1:
    if j > h:
        lat += 2
    else:
        lat += 1
print(lat)


'''string = input().split()
n = int(string[0])
h = int(string[1])
list1 = list(map(int, input().split()))
lat = 0
for students in list1:
    if students > h:
        lat += 2
    else:
        lat += 1
print(lat)'''
