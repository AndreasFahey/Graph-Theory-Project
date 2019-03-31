#Graph Theory Project 2019
#Shunting Yard Algorithm To Convert Regular Expressions from infix to postfix

#Andreas Fahey
#G00346830

#Shunting Yard Algorithm (SYA)
#Regular expressions from infix to postfix

def shunt(infix):
    """SYA To Convert Regular Expressions from infix to postfix"""

    specials = {
        "*": 30,
        "+": 25,
        "?": 20,
        ".": 15,
        "|": 10
    }

    #return postfix
    postfix = ""

    #operator stack
    stack = ""

    #for used to go through each char of the infix string
    for c in infix:
        #if ( push to stack
        if c == "(":
            stack = stack + c
        #if ) pop from stack and push to output
        elif c == ")":
            while stack[-1] != "(":
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        #if theres an operator push to stack
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        #regular characters to output
        else:
            postfix = postfix + c
    #pop remaining operator charcaters from stack
    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]
    
    return postfix 

#Thompsons Construction
#Will build nfas from postfix
#This algorithm used to determine whether state should be accepted or not
#Will Implement state and nfa classes
#Empty sets
class state:
    label1 = None
    edge1 = None
    edge2 = None

#Initial and accept state for each nfa
class nfa:
    initial = None
    accept = None

    #build new nfa constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

#This method turns a regular expression into a nfa
def compile(postfix):
    """Convert a regular expression (postfix) into an NFA"""

    nfaStack = []

    for c in postfix:
        if c == '*':
            #1 nfa from stack
            nfa1 = nfaStack.pop()
            #new initial and accept states
            initial = state() 
            accept = state()
            #joins new accept state
            initial.edge1 = nfa1.initial
            #joins old accept state to new
            initial.edge2 = accept
            #push new nfa to stack
            nfaStack.append(nfa(initial, accept))
        #Concat
        elif c == '.':
            #pops 2 nfas
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            #connects first nfa accept to second nfa initial 
            nfa1.accept.edge1 = nfa2.initial
            #push new nfa to stack
            nfaStack.append(nfa(nfa1.initial, nfa2.accept))

        elif c == '|':
            #pops 2 nfas
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()
            #create new initial state
            initial = state()
            #connects new 'initial' state to 2 nfas that were popped
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #create new accept state
            accept = state()
            #connects new 'accept' state to 2 nfas that were popped
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept
            #push new nfa to stack
            nfaStack.append(nfa(initial, accept))
        
        elif c == "+":
            #1 nfa from stack
            nfa1 = nfaStack.pop()
            #new initial and accept states
            initial = state()
            accept = state()
            #joins new initial state to nfa1
            initial.edge1 = nfa1.initial
            #joins old accept to new and initial
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #push new nfa to stack
            nfaStack.append(nfa(initial, accept))

        elif c == "?":
            #1 nfa from stack
            nfa1 = nfaStack.pop()
            #new initial and accept states
            initial = state()
            accept = state()
            #joins new initial state to nfa1
            initial.edge1 = nfa1.initial
            #joins old accept to new and initial
            initial.edge2 = accept 
            nfa1.accept.edge1 = accept
            #push new nfa to stack
            nfaStack.append(nfa(initial, accept))

        else:
            #new initial and accept states
            accept = state()
            initial = state()
            #joins initial state to accept state using an edge 'c'
            initial.label1 = c
            initial.edge1 = accept
            #push new nfa to stack
            nfaStack.append(nfa(initial, accept))

    return nfaStack.pop()

#Returns states that follow the edges
def followes(state):
    """Return states that can be reached by following the edges"""

    #new set with state as the only member
    states = set()
    states.add(state)
    #check if edges are empty (acceptable)
    if state.label1 is None:
        #if edge1 is a state
        if state.edge1 is not None:
            states |= followes(state.edge1)
        #if edge2 is a state
        if state.edge2 is not None:
            states |= followes(state.edge2)
    #return set
    return states
#Match string to infix
def match(infix, string):
    """String to infix regular expression"""

    postfix1 = shunt(infix)
    nfa = compile(postfix1)

    #current and next set of states
    curSet = set()
    nxtSet = set()
    #initial to current set
    curSet |= followes(nfa.initial)
    #loop through each character 1 by 1
    for s in string:
        #loop through current
        for c in curSet:
            #state check for s
            if c.label1 == s:
                #add edge1 to next
                nxtSet |= followes(c.edge1)
        #Current to Next
        curSet = nxtSet
        #Clear for next state
        nxtSet = set()
    
    return (nfa.accept in curSet)

#infixes = ['a.b.c*', 'a.b.c+', 'a.(b|d).c*', '(a.(b|d))', 'a.(b.b)*.c', 'a.b.c?']
#strings = ['', 'abc', 'abbc', 'abcc', 'abcd', 'abbcc', 'abd']

#User Input
#Number of Infixes (noi)
#Number of Strings (nos)
noi = int(input("Please Enter The Number of Infixes You Would Like to use: "))

count = 1

infixes = []
strings = []

#While for infix input
while noi > 0:
    infix = input("Please Enter Infix: ")
    infix = infix.replace("","")
    infixes.append(infix)
    count+=1
    noi -= 1

#Show what infixes user entered
print(infixes)

nos = int(input("Please Enter The Number of Strings You Would Like to use: "))

#While for string input
while nos > 0:
    string = input("Please Enter String: ")
    strings.append(string)
    nos -= 1

#Show what strings user entered
print (strings)

#loop for outcome
for i in infixes:
    for s in strings:
        print(match(i, s), i, s)

