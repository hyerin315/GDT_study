infile = open("files/txt_files/proverbs.txt", "r", encoding="UTF-8")
for line in infile: #line : 한 줄씩 read
    line = line.rstrip()
    word_list = line.split() #공백으로 자르기
    for word in word_list:
        print(word)

infile.close()

