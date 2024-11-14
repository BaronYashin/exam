print("Добрый день, Наталья Михацловна! Посчитаем средний балл наших спиногрызов?")
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
OtsortirovannySpisok = list(students)
Spisok = sorted(OtsortirovannySpisok)
print(Spisok)
SrAaron = (sum(grades[0])/len(grades[0]))
SrBilbo = (sum(grades[1])/len(grades[1]))
SrJohnny = (sum(grades[2])/len(grades[2]))
SrKhendrik = (sum(grades[3])/len(grades[3]))
SrSveta = (sum(grades[4])/len(grades[4]))
print("Средний балл учеников;", "Арон = ", SrAaron, "Бильбо = ", SrBilbo, "Джони = ", SrJohnny, "Света = ", SrSveta) # для себя
NewBall = [SrAaron, SrBilbo, SrJohnny, SrKhendrik, SrSveta]
print(NewBall)
SredniyBall = {Spisok[0]:NewBall[0], Spisok[1]:NewBall[1], Spisok[2]:NewBall[2], Spisok[3]:NewBall[3], Spisok[4]:NewBall[4]}
print(SredniyBall)