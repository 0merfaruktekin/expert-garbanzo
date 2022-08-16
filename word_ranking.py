list1=[]
list2=[]
list=[]
f=open("words.txt","r")
list1=f.readlines()
def bubblesort(liste):
    for i in range(len(liste)):
        temp1=0
        temp2=0
        for x in range(len(liste)-1):
            if liste[x][1]<=liste[x+1][1]:
                temp1=liste[x]
                temp2=liste[x+1]
                liste[x+1]=temp1
                liste[x]=temp2
    return liste
for i in range(len(list1)):
    list1[i]=list1[i].strip()
letters={"a":0,"b":0,"c":0,"ç":0,"d":0,"e":0,"f":0,"g":0,"ğ":0,"h":0,"ı":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"ö":0,"p":0,"r":0,"q":0,"w":0,"s":0,"ş":0,"t":0,"u":0,"ü":0,"v":0,"x":0,"y":0,"z":0}
for word in list1:
    for letter in word:
        if letter in letters:
            letters[letter]+=1
for word in list1:
    value=0
    for letter in word:
        if word.count(letter)>=2:
            value+=letters[letter]/2
        else:
            value+=letters[letter]
    list2.append(value)
for i in range(len(list1)):
    list.append([list1[i],list2[i]])
def reset():
    list.clear()
    for i in range(len(list1)):
        list.append([list1[i],list2[i]])

