ffrom random import*
import string 
def izmenauser(user:list,password:list)->list:
    """
    Kasutaja nimi muutmine
    """
    nimi=input("Sisestage kasutaja nimi: ")
    if nimi in user:
        nuser=input("Sisestage uus kasutaja nimi: ")
        user[user.index(nimi)]=nuser
        print("See on teie uus kasutaja nimi:",nuser)
    else:
        print("Vale")
    return nuser



def izmenapass(user:list,password:list)->list:
    """
    Parooli muutmine
    """
    nimi=input("Sisestage kasutajanimi: ")
    password=input("Sisestage parool: ")
    if nimi in user and user[nimi]==password:
        npass=input("Sisestage uss parool: ")
        user[nimi]==npass
        print("See on teie uus parool",npass)
    else:
        print("Vale")
    return npass





def avtor(user:list,password:list)->list:
    """
    Kasutaja autoriseerimine
    """
    nimi=input("Sisestage kasutajanimi:")
    sala=input("Sisestage Parool: ")
    if nimi in user:
        ind=user.index(nimi)
        if sala==password[ind]:
            print("Tere Tulemast")
        else:
            print("Vale parool")
    else:
        print("Kasutajanime ei leitud")
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
    """
    Registreerimine
    """
    nimi=input("Sisestage kasutajanimi: ")
    v=int(input("1-Parooli tegemine, 2-Luua"))
    if v==1:
        v2=input("Sisestage Parool: ")
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):   # пароль содержит хотя бы одну цифру
            return False
        if not any(char.isupper() for char in password):   # пароль содержит одну заглавную букву
            return False
        else:
            print("Vale")
        return True
    else:
        salasona=Salasona(5)
        user.append(nimi)
        password.append(salasona)
    return user,password

