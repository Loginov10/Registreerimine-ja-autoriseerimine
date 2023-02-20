from random import*
import string 
def izmenauser(user:list,password:list)->list:
    """
    смена пользователя
    """
    nimi=input("Введите имя:")
    sala=input("Введите пароль: ")
    if nimi in user:
        ind=user.index(nimi)
        if sala==password[ind]:
            print("Добро пожаловать")
            nimi1=input("Введите новое имя: ")           
            for i in range(0,len(user)):
                user=user.insert(user[i],user[nimi1])
                print(user)
        else:
            print("Неверный пароль")
    else:
        print("Имя не найденно")




def izmenapass(user:list,password:list)->list:
    """
    смена пароля
    """
    user=input("Введите ваш логин: \n")   #\n строка вниз
    if user in password:
         password=input("Введите ваш пароль: \n")
         if password==password[password]:
              print(password)
              print("Смена пароля")
              print("Введите ваш новый пароль")
              password = input()
              password[password]=password    #update обновляет параметры
              print(password)
         else:
              print("Пароль неверный")
    else:
         print("Логин не найден")               
    return password




def avtor(user:list,password:list)->list:
    """
    Авторизация пользователя
    """
    nimi=input("Введите имя:")
    sala=input("Введите пароль: ")
    if nimi in user:
        ind=user.index(nimi)
        if sala==password[ind]:
            print("Добро пожаловать")
        else:
            print("Неверный пароль")
    else:
        print("Имя не найденно")
    return nimi,sala


def Salasona(k: int):
  sala=""
  for i in range(k):
    t=choice(string.ascii_letters) #Aa...Zz
    num=choice([1,2,3,4,5,6,7,8,9,0])
    sym=choice(["*","-",".","!",","])
    t_num=[t,str(num),sym]
    sala+=choice(t_num)
  return sala

def registr(user:list,password:list):
    nimi=input("Введите имя: ")
    v=int(input("1-Сделать пароль, 2-Сгенерировать"))
    if v==1:
        pass
    else:
        salasona=Salasona(5)
        user.append(nimi)
        password.append(salasona)



