# evvery five words in a file after that add \n 
f = open("abc.txt","w")
f.write("I am going to market")
f=open("abc.txt","r")
data = f.readlines()
for i in data:
    words = i.split()
    for j in range(0, len(words), 5):
        data.append(' '.join(words[j:j+5]) + '\n')

    
f.close()
print(data)