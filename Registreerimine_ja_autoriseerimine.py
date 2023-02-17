from module import*
user=["gena","valja"]
password=["12345","gaga"]
while True:
    print("1-Регистрация, 2-Авторизация, 3-Выход, 4-Смена пароля")
    a=int(input())
    if a==1:
        user,password=registr(user,password)
    
    elif a==2:
        avtor(user,password)

    elif a==3:
        print("Выход")
        break
    
    elif a==4:
        print("Смена пароля")
        izmena(user,password)
      
    else:
        print("Введи правильно")

   
    
    
    
