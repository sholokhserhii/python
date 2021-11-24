#Lesson 1, task 6
rasst_first=float(input("Сколько км пробежал спортсмен в первый день? "))
rasst_dostig=float(input("Какого расстояния спортсмен должен достигнуть? "))
rasst_tekush=rasst_first
den=1
while rasst_tekush<rasst_dostig:
    rasst_tekush=rasst_tekush * 1.1
    den +=1
print('На ',den,'-й день спортсмен пробежал не менее ',rasst_dostig,' км - ',"{:.2f}".format(rasst_tekush)," км",sep='')