#Lesson 1, task 4
user_number=int(input('Введите целое положительное число (можно большое) '))
celaya_chast=user_number//10
ostatok=user_number%10
max_cifra=ostatok
while celaya_chast>0:
    ostatok=celaya_chast%10
    if ostatok>max_cifra:
        max_cifra=ostatok
    celaya_chast=celaya_chast//10
print('Наибольшая цифра в числе',max_cifra)
