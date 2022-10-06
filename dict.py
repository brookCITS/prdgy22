dictionary = {'212': "New York", '301': "Maryland", '202': "DC"}

try:
    file = open('myfile.txt')
    #file.write(str(dictionary))
    file.close()

except:
    print("Unable to append to file")

print("Program Still Running!")
