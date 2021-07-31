letters = ['e', 'd', 'c', 'b', 'a']

#인덱스
print(letters)
print(letters[0])
print(letters[1])
print(letters[2])

#리스트를 가져와 반복 출력
for i in letters:
    print(i, end=" ")
print()

#길이를 가져와 반복 출력
for j in range(len(letters)):
    print(letters[j], end=" ")
print()

#슬라이싱
print(letters[:3])
print(letters[3:])
print(letters[:])

#리스트 값 변경
letters[1] = 'Bravo'
print(letters)

#리스트 값 추가
letters.append('f')
letters.append('Good')
print(letters)

#리스트 원하는 위치에 값 추가
letters.insert(1, "b")
print(letters)

#리스트 원하는 값 삭제하기
letters.remove('b')
print(letters)

#리스트 원하는 값 인덱스로 삭제하기
del letters[1]
print(letters)

#리스트 마지막 항목 삭제 후 반환 (잘라내기)
last_letters = letters.pop()
print(last_letters)
print(letters)

#리스트 값 탐색하기
if "Bravo" in letters:
    print("True")
else:
    print("False")

#리스트 값 인덱스 탐색
print(letters.index("c"))

#리스트 값 정렬
print(letters)
letters.sort()
print(letters)

#정렬된 리스트 변수 설정
letters = ['e', 'd', 'c', 'b', 'a']
print("정렬")
new_letters = sorted(letters)
print(new_letters)

#반대로 정렬
new_letters_reverse =  sorted(new_letters, reverse=True)
print(new_letters_reverse)


