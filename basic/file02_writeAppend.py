#텍스트 쓰기
outfile = open("txt_files/phonenumber.txt", "w")
outfile.write("홍길동 010-1235-6789\n")
outfile.write("김연아 010-4321-5789\n")
outfile.write("배철수 010-6430-2876\n")
print(outfile)

outfile.close()

#텍스트 추가하기
outfile = open("txt_files/phonenumber.txt", "a")
outfile.write("김영희 010-1235-6789\n")
outfile.write("이순신 010-4321-5789\n")
outfile.write("김유신 010-6430-2876\n")
print(outfile)

outfile.close()

#전체 텍스트 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readline().rstrip()
while lines != "":
    print(lines)
    lines = infile.readline().rstrip()

infile.close()

#읽고 쓰기
outfile = open("txt_files/phonenumber.txt", "r+")
outfile.write("홍길동 010-1235-6789\n")
outfile.write("김연아 010-4321-5789\n")
outfile.write("배철수 010-6430-2813\n")
print(outfile)

outfile.close()

#전체 텍스트 읽기
infile = open("txt_files/phonenumber.txt", "r")
lines = infile.readline().rstrip()
while lines != "":
    print(lines)
    lines = infile.readline().rstrip()

infile.close()