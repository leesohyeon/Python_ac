import codecs

file = codecs.open("phone.txt",'w',"UTF-8")

file.write("뽀로로 010-1234-5678\n")
file.write("뽀로로 010-1234-5678\n")
file.write("뽀로로 010-1234-5678\n")

file.close()