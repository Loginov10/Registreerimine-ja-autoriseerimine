from module import*
user=["gena","valja"]
password=["12345","gaga"]
while True:
    print("1-Регистрация, 2-Авторизация, 3-Выход")
    a=int(input())
    if a==1:
        user,password=registr(user,password)
    
    elif a==2:
        avtor(user,password)

    elif a==3:
        print("Выход")
        #
   
    
    
    
