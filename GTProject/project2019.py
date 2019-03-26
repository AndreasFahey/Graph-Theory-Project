#Graph Theory Project 2019
#Shunting Yard Algorithm To Convert Regular Expressions from infix to postfix

#Andreas Fahey
#G00346830

def shunt(infix):
    """SYA To Convert Regular Expressions from infix to postfix"""

    specials = {
        "*": 50,
        ".": 40,
        "|": 30
    }

    postfix = ""
    stack = ""

    for i in infix:
        if i == "(":
            stack += i
        elif i == ")":
            while stack[-1] != "(":
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif i in specials:
            while stack and specials.get(i, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + i
        else:
            postfix = postfix + i

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]
    
    return postfix 
    
