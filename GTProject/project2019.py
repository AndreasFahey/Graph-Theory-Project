#Graph Theory Project 2019
#Shunting Yard Algorithm To Convert Regular Expressions from infix to postfix

#Andreas Fahey
#G00346830

def shunt(infix):
    """SYA To Convert Regular Expressions from infix to postfix"""

    specials = {
        "+": 70,
        "?": 60,
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

#print(shunt("a.(b|d).c*"))

class state:
    label1 = None
    edge1 = None
    edge2 = None

class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(postfix):
    """Compile postfix regular expression NFA"""

    stack = []

    for c in postfix:
        if c == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept.edge1 = nfa2.initial
            stack.append(nfa(nfa1.initial, nfa2.accept))

        elif c == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            stack.append(nfa(initial, accept))

        elif c == '*':
            nfa1 = stack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            stack.append(nfa(initial, accept))

        elif c == "+":
            nfa1 = stack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            stack.append(nfa(initial, accept))

        elif c == "?":
            nfa1 = stack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept 
            nfa1.accept.edge1 = accept
            stack.append(nfa(initial, accept))

        else:
            accept = state()
            initial = state()
            initial.label1 = c
            initial.edge1 = accept
            stack.append(nfa(initial, accept))

    return stack.pop()

#print(compile("ab.cd.|"))

def followes(state):
    """Return states from the state following e arrows"""

    states = set()
    states.add(state)

    if state.label is None:
        if state.edge1 is not None:
            states |= followes(state.edge1)
        if state.edge2 is not None:
            states |= followes(state.edge2)

    return states



