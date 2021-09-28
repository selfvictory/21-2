#sectin 23~31 실습

#section_026.py

print('section_026\n')
numbers =[0,1,2,3,4,5]
animals = ['개','고양이','토끼','다람쥐']

print(numbers)
print(animals)

#numbers의 첫번째 항목 출력
print(numbers[0])

#animals의 두번째 항목 출력
print(animals[2])

#animals의 끝에서 두번째 항목 출력
print(animals[-2])
print('\n')




#section_027.py

print('section_027\n')

#animals 2번을 '거북이'로 변경 출력
animals[2] = '거북이'
print(animals)

#animals 뒤에 '토끼' 추가하여 zoo에 저장 출력
zoo = animals +['토끼']
print(zoo)
print(animals)
print('\n')



#section_028.py

print('section_028\n')

#animals 1~2번 항목 zoo에 저장 후 출력
zoo = animals[1:3]
print(zoo)

#슬라이싱을 사용하여 animals전체 출력
print(animals)
print(animals[0:4])
print('\n')



#section_029.py
print('section_029\n')

#animals 에서 '거북이'와 '토끼'위치 출력(index)
print("거북이의 위치:",animals.index('거북이'))
#print("토끼의 위치:",animals.index('토끼'))
print("다람쥐의 위치:",animals.index('다람쥐'))

#animals에서 '원숭이'추가후 출력(append)
animals.append('원숭이')
print(animals)

#animals 3번 위치에 '펭귄' 추가 후 출력(insert)
animals.insert(3,'펭귄')
print(animals)

#numbers에 [6,7,8]추가 후 출력(extend)
numbers.extend([6,7,8])
print(numbers)
print('\n')





#section_030.py

print('section_030\n')

#numbers, animals 각각 정렬후 출력(sort)
numbers.sort()
animals.sort()
print(numbers)
print(animals)

#numbers 역순 정렬 후 출력(reverse)
numbers.reverse()
print(numbers)

numbers2 = [4,1,3,7,-2]
numbers2.reverse()
print(numbers2)

#animals 맨 마지막 항목을 빼내서 my_animal에 저장후 두 리스트 출력(pop)
my_animal = animals.pop()
print(my_animal)
print(animals)

#numbers 에서 4제거 후 출력(remove)
numbers.remove(4)
print(numbers)

#animals에 2번 항목과 맨 뒤에 '펭귄' 추가 후, '펭귄' 항목수 출력(count)
animals.insert(2,'펭귄')
animals.append('펭귄')
print(animals.count('펭귄'))
print('\n')





#section_031.py
print('section_031\n')

#numbers, animals 각 리스트 길이 출력
print(len(numbers))
print(len(animals))
print('\n')

#numbers, animals 각 리스트 최대값 출력
print(max(numbers))
print(max(animals))

#numbers, animals 각 리스트 최소값 출력
print(min(numbers))
print(min(animals))
print('\n')

#numbers의 합 출력
print(sum(numbers))
print('\n')

#numbers오름차순으로 변경한 리스트 출력, numbers자체는 불변,(sorted)
print(sorted(numbers))
print(numbers)
print('\n')

#문자열 'Hello Python'을 리스트로 변경
print(list("Hello Python"))


