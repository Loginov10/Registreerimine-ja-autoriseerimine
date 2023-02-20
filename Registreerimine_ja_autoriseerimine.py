from module import*
user=["vena"]
password=["12345"]
while True:
    print("1-registreerimine, 2-Autoriseerimine, 3-Väljapääs, 4-Parooli muutmine, 5-Kasutajanimi muutmine")
    a=int(input())
    if a==1:
       registr(user,password)
    
    elif a==2:
        avtor(user,password)

    elif a==3:
        print("Väljapää")
        break
    
    elif a==4:
        print("Parooli muutmine")
        izmenapass(password,user)

    elif a==5:
        print("Kasutajanimi muutmine")
        izmenauser(user,password)
      
    else:
        print("Sisestage õigesti")
   
    
    
    
