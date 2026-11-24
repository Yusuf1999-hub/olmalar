# lst = ["Karim", "Valiyev", 12]

# dct = {"name":["Karim", "Vali"], "second":"Valiyev", "age":12, "name":"Olim"}
# print(dct)

# ---------------------------

# moshina = {
#     "brand" : "bmw",
#     "color" : "black",
#     "year"  : 2025,
#     "price" : 25000
# }

# moshina['price'] = 145000
# moshina['motor'] = "V8"

# print(moshina)

# -----------------------------

# dct = {}

# lst = [("Aziz", 5000), ("Karim", 2500), ("Aziz", 500), ("Vali", 100), ("Vali", 50), ("Karim",100)]

# for inson, maosh in lst:
#     if inson not in dct:
#         # dct[inson] = 1
#         dct[inson] = maosh
#     else:
#         # dct[inson] += 1
#         dct[inson] += maosh

# print(dct)

# ------------------------------

# lugat = {}

# for i in range(int(input("Nechta so'z kiritasiz: "))):
#     english = input("Ingliz: ")
#     uzbek = input("O'zbek: ")
#     lugat[english] = uzbek

# print(lugat)

# -----------------------------

# lst = [
#     {"name":"Javlon", "age":22},
#     {"name":"Avaz", "age":12},
#     {"name":"Ali", "age":19},
#     {"name":"Axror", "age":15}
# ]

# for shaxs in lst.copy():
#     if shaxs['age'] < 18:
#         lst.remove(shaxs)

# print(lst)

# --------------------------------

# dct = {
#     "Aziz" : 56,
#     "Karim" : 17,
#     "Vali" : 85,
#     "Olim" : 14,
#     "Doston" : 80
# }

# katta = ("", 0)
# for ism, score in dct.items():
#     if katta[1] < score:
#         katta = (ism, score)
# print(katta)

# -----------------------------------

# dct = {
#     "Aziz" : 56,
#     "Karim" : 17,
#     "Vali" : 85,
#     "Olim" : 14,
#     "Doston" : 80
# }

# score = min(dct.values())

# for ism, bal in dct.copy().items():
#     if bal == score:
#         dct.pop(ism)


# natija = dct.pop(min(dct, key=dct.get))
# print(dct)
# print(natija)

# -------------------

dct = {"name":"Karim",
       "yosh" : 12,
       "color":"yellow"}

qiymat = dct.pop("yosh")
dct['age'] = qiymat
print(dct)