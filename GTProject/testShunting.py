#Graph Theory 2019
#Andreas Fahey - G00346830
#My Shunting Yard Algorithm Test

def shunt(infix):

    specials = {
        "*": 50,
        "+": 40,
        "?": 30,
        ".": 20,
        "|": 10
    }

    #postfix and stack created as empty strings
    postfix = ""
    stack = ""

    #for used to go through each char of the infix string
    for c in infix:
        #if c is ( add to stack
        if c == "(":
            stack = stack + c
            #other
        elif c == ")":
            while stack[-1] != "(":
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
            #if c is in the special charcter library
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
            #other - add c to the postfix
        else:
            postfix = postfix + c

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]
    #returns regular expression in postfix
    return postfix 
#print result
print(shunt("a.(b|d).c*.d"))