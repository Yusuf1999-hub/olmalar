ptr = open("test.txt")

st = set()

data = ptr.read().split("\n")
for qator in data:
    domen = qator.split('.')[-1]
    st.add(f".{domen}")
print(st)

ptr.close()