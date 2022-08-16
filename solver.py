import word_ranking as w
def suggestion():
    suggestions=[]
    w.bubblesort(new_list)
    for i in range(5):
        suggestions.append(new_list[i])
    return suggestions
new_list=w.list
def eliminate(l):
    global new_list
    for letter in l:
        for word in new_list:
            if word[0].find(letter)!=-1:
                word[1]=0
    return new_list
def checkpos_green(position,letter):
    global new_list
    for word in new_list:
        if word[0][position] != letter:
            word[1]=0
                           
    return new_list
def checkpos_yellow(position,letter):
    global new_list
    for word in new_list:
        if word[0][position] == letter or word[0].find(letter)==-1:
            word[1]=0
    return new_list



                
