import calendar

cal=calendar.Calendar(firstweekday=0)

count=0

monthnum=[]
mon=[]

month={1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

for m in range(1,12):
    day=cal.itermonthdays(2018,m)
    for n in day:
        if n==0:continue
        num=calendar.weekday(2018,m,n)
        if num==6:
            count+=1
            if count>=5:
                monthnum.append(m)
                break

for i in monthnum:
    mon.append(month[i])

print(mon)




