#read from python
#1
#ipsum_file = open("files/ipsum.txt")
#ipsum_file.seek(0)

#for line in ipsum_file:
    #print(line)
    #line = line.rstrip()
    #count = len(line.split(" "))
    #print(line + " | "+str(count))
#print(ipsum_file[1])
#2
#ipsum_file.seek(0)
#lines = ipsum_file.readlines()
#print(lines)
#print(lines[0])

words = ['Hello', 'There', 'how', 'are', 'you?']

index = 1
with open('files/write.txt', 'w') as file:
    #file.write("I\nlove\nPython\nso\nmuch\n")
    for item in words:
        file.write(str(index)+") "+item+"\n")
        index+=1
