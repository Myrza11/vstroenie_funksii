'''nambers = [1,'2',3,'4',5,'6a',7,'8']

for i in range(-5,5):
	if int(I) % 2 == 0:
	    print(nambers[8]/i)
try:
	for i in range(-5,5):
	if int(I) % 2 == 0:
	    print(nambers[8]/i)
except SyntaxError:
	print("Найдена ошибка синтаксическая")
except IndentationError:
	print("Найдена ошибка")
except TypeError:
	print("найдена ошибка")
except ZeroDivisionError:
	print("на ноль делить нельзя")
except NameError:
	print("ошибка имён")
else:
	print("нет ошибок")
finally:
	print("в любом случае")

#первое задание
values = ("Rzakov 32", 10, 1005, ["tables", "chairs"], 23.00)

w = []

for i in values:
	try:
		set(i)
		w.append(True)
	except TypeError:
	    w.append(False)
print(w)
print(all(w))		





#втарое задание
a = input("введите число")
b = input("введите число")
c = input("введите число")
e = input("введите число")
f = input("введите число")
k = []
k.append(a)
k.append(b)
k.append(c)
k.append(e)
k.append(f)
print(min(k))
print(k)




#третье задание
w = ["all","any","abs","min","eval","reversed","max","slice","round"]
d = input("напиши функцию: ")
i=0
try:
	while w[i] != d:
	    print("не правильно")
	    i+=10
	else:
		print(d, "правильно")
except IndexError:
	print("у вас не правильно")

#четвёртое задание
a = float(input("кредит можно брать больше 50000: "))
b = a / 100 * 3.47
print(round(b, 2))


#пятое задание
nambers = [1,'2',3,'4',5,'6a',7,'8']

for i in range(-5,5):
	if int(I) % 2 == 0:
	    print(nambers[8]/i)


#пятое задание
at = 10
iin = 15
wo = 20
try:
for e in range(-at, at):
	print(wo / e)
	if at > '5':
		print(at > 5)
except: SyntaxError
	print('errors')
'''	

#шестое задание
lst = []
try:
	for i in range(10):
	    lst.append(i)
	    a = list(reversed(lst))
	    sls_obj = slice('0','8')
	    print(а[sls_obj])
except NameError:
	print("у вас ошибка")
except SyntaxError:
	print("у вас ошибка")
except:
	print("у вас ошибка")
finally:
	print("у вас ошибка")
    


#сeдьмое задание
a = (0)
b = (1,)
numbers = []
try:
	while b < a:
	    numbers += b
	    b += 1
except TypeError:
	print("у вас ошибка")

#восьмое задание
dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
try:
    for x in dict_.keys():
        x + 'abc'
except IndentationError:
	print("у вас ошибка")
except TypeError:
	print("у вас ошибка")
finally:
	print("у вас ошибка")

