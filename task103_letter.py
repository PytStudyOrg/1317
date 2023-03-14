s=input ("Введите в буквы")
x=""
for c in x:
    if c == "а":
        x += "б"
    elif c =="б":
        x +="а" 
    elif c =="А":
        x +="Б"
    elif c =="Б":
        x +="А" 
    elif c =="с":
        x +="с"
    elif c =="С":
        x +="С"
    else:
        x +="с" 
print (x)    