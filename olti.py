def fourth(a:list) -> list:
    st = set()
    for email in data:
        st.add(email.split("@")[1])
    return list(st)

data = ["salom@gmail.com", "malina@mail.com", "karam@gmail.com"]
print(fourth(data))