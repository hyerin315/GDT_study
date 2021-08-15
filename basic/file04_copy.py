infilename = './txt_files/'+(input("복사할 파일 이름을 입력하시오 : "))
outfilename = './txt_files/'+(input("저장될 파일 이름을 입력하시오 : "))

infile = open(infilename, "r")
outfile = open(outfilename, "w")

file = infile.read()
outfile.write(file)

infile.close()
outfile.close()