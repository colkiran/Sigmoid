
def callMe():
    print(f"Apple from Ooty")


def fun(fnc):
    print("Hello")
    fnc()
    print("hi")
    print('_' * 40)

    def defineMe():
        print(f"Oranges from Kanpur")

    return defineMe


def funCallback(fnc):
    print("Mera Barath Mahan")
    fnc()               # Call back
    print("India is Great")


funCallback(fun(callMe))

