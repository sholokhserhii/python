#Lesson 1, task 2
vremya_sekund=int(input("Введите время в секундах "))
hours=vremya_sekund//3600
minuts=(vremya_sekund%3600)//60
sekunds=(vremya_sekund%3600)%60
print(f"{hours}:{minuts}:{sekunds}")