
def outerFun(greet):        # HOF - higher order function

    # Simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun


engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")

engGrt("Sachin")
hndGrt("Jadeja")






print("-" * 60)

outerFun("Greetings")("Sachin")
