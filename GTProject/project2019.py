#Graph Theory Project 2019
#Shunting Yard Algorithm To Convert Regular Expressions from infix to postfix

#Andreas Fahey
#G00346830

def shunt(infix):
    """SYA To Convert Regular Expressions from infix to postfix"""

    specials = {
        "*": 30,
        "+": 25,
        "?": 20,
        ".": 15,
        "|": 10
    }

    postfix = ""
    stack = ""

    for c in infix:
        if c == "(":
            stack = stack + c
        elif c == ")":
            while stack[-1] != "(":
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c

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

    nfaStack = []

    for c in postfix:
        if c == '*':
            nfa1 = nfaStack.pop()
            initial, accept = state(), state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            nfaStack.append(nfa(initial, accept))


        elif c == '.':
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            nfa1.accept.edge1 = nfa2.initial
            nfaStack.append(nfa(nfa1.initial, nfa2.accept))

        elif c == '|':
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            nfaStack.append(nfa(initial, accept))

        elif c == "+":
            nfa1 = nfaStack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            nfaStack.append(nfa(initial, accept))

        elif c == "?":
            nfa1 = nfaStack.pop()
            initial = state()
            accept = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = accept 
            nfa1.accept.edge1 = accept
            nfaStack.append(nfa(initial, accept))

        else:
            accept = state()
            initial = state()
            initial.label1 = c
            initial.edge1 = accept
            nfaStack.append(nfa(initial, accept))

    return nfaStack.pop()

#print(compile("ab.cd.|"))

def followes(state):
    """Return states from the state following e arrows"""

    states = set()
    states.add(state)

    if state.label1 is None:
        if state.edge1 is not None:
            states |= followes(state.edge1)
        if state.edge2 is not None:
            states |= followes(state.edge2)

    return states

def match(infix, string):
    """String to infix regular expression"""

    postfix1 = shunt(infix)
    nfa = compile(postfix1)

    curSet = set()
    nxtSet = set()

    curSet |= followes(nfa.initial)

    for s in string:
        for c in curSet:
            if c.label1 == s:
                nxtSet |= followes(c.edge1)

        curSet = nxtSet
        nxtSet = set()

    return (nfa.accept in curSet)

infixes = ['a.b.c*', 'a.b.c+', 'a.(b|d).c*', '(a.(b|d))', 'a.(b.b)*.c', 'a.b.c?']
strings = ['', 'abc', 'abbc', 'abcc', 'abad', 'abbcc', 'ab']

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)

