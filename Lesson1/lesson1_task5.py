#Lesson 1, task 5
vyruchka=float(input('Какая сегодня выручка? '))
izderzhki=float(input('Какие сегодня издержки? '))
if vyruchka>izderzhki:
    print('Мы сегодня с прибылью в ',"{:.2f}".format(vyruchka-izderzhki),' рублей')
    print("Рентабельность составляет", "{:.3f}".format((vyruchka-izderzhki)/vyruchka))
    worker_number=int(input("Сколько у нас сегодня работников? "))
    print("Каждый сотрудник сегодня принес", "{:.2f}".format((vyruchka-izderzhki)/worker_number)," рублей прибыли!")
else:
    print("Мы сегодня в убытках на", "{:.2f}".format(izderzhki-vyruchka)," рублей")