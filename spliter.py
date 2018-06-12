from condition import conditions
f = open(r'C:\Users\User\Desktop\data\data3.txt', encoding="utf-8-sig")
data = f.readlines()  # read from doc
doc = []
x = 0
def addDes():
    global x
    for line in data:
        words = line.split()  # spilt individual words
        print(words)
        if ((words[0][0].isupper()and words[0][1].isdigit()) or words[0][0].isdigit()) and len(words[0])>=3 : # check for not 2 lines description
            conditions(words)
            doc.append(words)
            x = x+1
        else :
            for i in range(len(words)):#append to previous lines
                doc[x-1].append(words[i])
            continue
        
    print(doc)

def write():
    global x
    w = open(r'C:\Users\User\Desktop\data\info2.txt', "w",
             encoding="utf-8")  # write word to text file
    for i in range(x):
        for j in range(0, 3):
            w.write(doc[i][j]+";")
        for j in range(3, len(doc[i])):
            w.write(doc[i][j]+" ")
        w.write('\n')


addDes()
write()
