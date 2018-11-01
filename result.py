def myfunc(*x, dws = []):
	new_x = []
	x2=[]
	for i in x:
		if type(i) == list:
			x2 = x2 + i
		else:
			x2.append(i)
	for i in  x2:
		if i not in new_x:
			if i not in dws:
				new_x.append(i)
	return new_x

print(myfunc([1, 3, 2, 1, 2]))

if __name__ == '__main__':
	assert myfunc([1, 3, 2, 1, 2]) == [1, 3, 2], "Другая ошибка"
	assert myfunc(['a', 'b', 'a', 1]) == ['a', 'b', 1], "Ошибка работы с char"
	assert myfunc([1, 1, 3, 2], [1, 3, 6], dws = [2]) == [1, 3, 6], "Проблема с объединением двух list объектов"
	assert myfunc(['a', 'b', 'a', 1], 1, 2, 'a', dws = ['c']) == ['a', 'b', 1, 2], "Проблема с объедиением list с другими объектами"
