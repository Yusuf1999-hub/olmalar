# set("145") -> {'1','4','5'}
# set("144") -> {'1','4'}
# set("52145") -> {'5','2','1','4'}
# set("333") -> {'3'}

son = int(input("Uch honali son kiriting: ")) 
if 100<=son<=999:
    a = son % 10 
    b = son // 10 % 10
    c = son // 100 % 10

    if a!=b and b!=c and a!=c:
        print("Bir hil emas")
    else:
        print("Shartga qanoatlanmadi")
else:
    print("Uch honali son kiritmadingiz!")