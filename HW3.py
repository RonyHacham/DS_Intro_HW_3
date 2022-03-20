#HW3_1
def read_line(n, file):
    if type(n)!= int:
        return ("invalid input detected")
    try:
        fhand = open(file)  
    except:
        return ("file not found")
    count=1
    for line in fhand:
        if (count==n):
            return (line)
        else:
            count=count+1
    return("line "+str(n)+" doesn't exist")


#HW3_2
def longest_words(file):
    try:
        fhand = open(file)  
    except:
        print ("file not found")
        return([])
    listf= ["","","","",""]
    for line in fhand:
        line=line.rstrip()
        line=line.replace("."," ")
        line=line.replace(","," ")
        line=line.replace("-"," ")
        line=line.replace("("," ")
        line=line.replace(")"," ")
        line=line.replace("'"," ")
        words=line.split()
        for word in words:
            if len(word)>len(listf[0]):
                listf[4]=listf[3]
                listf[3]=listf[2]
                listf[2]=listf[1]
                listf[1]=listf[0]
                listf[0]=word
            elif len(word)>len(listf[1]):
                listf[4]=listf[3]
                listf[3]=listf[2]
                listf[2]=listf[1]
                listf[1]=word
            elif len(word)>len(listf[2]):
                listf[4]=listf[3]
                listf[3]=listf[2]
                listf[2]=word
            elif len(word)>len(listf[3]):
                listf[4]=listf[3]
                listf[3]=word
            elif len(word)>len(listf[4]):
                listf[4]=word
    return(listf)
            
 




