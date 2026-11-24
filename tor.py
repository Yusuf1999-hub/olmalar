# tpl = ("salom", 23, "foundation", True)

# tpl = list(tpl)
# tpl[0] = 12
# tpl = tuple(tpl)
# print(tpl)

# for i in tpl:
#     print(i)

# --------------------------

# lst = [(12,32,34), (23,1,12), (1,45,23)]
# for tpl in lst:
#     print(max(tpl))
# new = [max(tpl) for tpl in lst]
# print(new)


lst = [(1,2), ('salom', 45), (12,12,12), (54,34)]
for index, tpl in enumerate(lst):
    tpl = list(tpl)
    tpl.append(15)
    tpl = tuple(tpl)
    lst[index] = tpl
print(lst)