
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun


engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

kanGrtTgr = kanGrt("tiger")
kanGrtlion = kanGrt("lion")
kanGrtbear = kanGrt("bear")

kanGrtTgr("Prabhakar")
kanGrtlion("Vishnuvardhan")
kanGrtbear("Anil")

"""
engGrtSngArw = engGrt("----->")
engGrtDblArw = engGrt("=====>>")
hndGrtSngArw = hndGrt("------>")
hndGrtDblArw = hndGrt("=====>>")

engGrtSngArw("Kapil")
engGrtDblArw("Sunil")

hndGrtSngArw("Virat")
hndGrtDblArw("Rohit")




print("-" * 60)
outerFun("Welcome")("----->")("Rahul")

"""