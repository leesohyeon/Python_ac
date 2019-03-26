file = open("phone.txt",'a')

for i in range(5,8):
    data = "%d line\n"%i
    file.write(data)

file.close()