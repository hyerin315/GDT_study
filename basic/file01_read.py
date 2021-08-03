#전체 텍스트 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.read()
print(lines)

infile.close()

#전체 데이터 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readlines()
print(lines)

infile.close()

#한 줄 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readline()
print(lines)

infile.close()

#반복해서 한 줄 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readline().rstrip()
while lines != "":
    print(lines)
    lines = infile.readline().rstrip()

infile.close()

#반복해서 한 줄 읽기 (end="" 사용)
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readline()
while lines != "":
    print(lines, end="")
    lines = infile.readline()

infile.close()