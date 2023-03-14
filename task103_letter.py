s=input ("Введите в буквы")
x=""
for c in x:
    if c == "а":
        x += "б"
    elif c=="б":
        x+="а" 
    elif c=="А":
        x+="Б"
    elif c=="Б":
        x+="А" 
    elif c=="C":
        x+="с"
    else:
        x+="с" 
print (x)    