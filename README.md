# Graph-Theory-Project

This is My Graph Theory Project Yr3

Andreas Fahey

G00346830

In the project file i have supplied 2 python files one testing the shunting yard algorithm alone and another the complete project including thompsons construction. 

Ive also supplied a Text Doc called References.txt which includes my research and references that aided me and gave me a better understanding of the task at hand. Lecture Videos also helped very much so throughout the coding and understanding of coding python.

*SHUNTING YARD ALGORITHM*

Developer: Edsger Dijkstra.
This algorithm converts an infix expression into a postfix expression.
Stack is used in this algorithm to hold operators not numbers. The purpose of stack in this algorithm is to reverse the order of operators in the expression. It also serves as a storage structure as no operator can be printed until both operands appear.

http://www.oxfordmathcenter.com/drupal7/node/628 

Rules:

1.If the incoming symbols is an operand, print it..

2.If the incoming symbol is a left parenthesis, push it on the stack.

3.If the incoming symbol is a right parenthesis: discard the right parenthesis, pop and print the stack symbols until you see a left parenthesis. Pop the left parenthesis and discard it.

4.If the incoming symbol is an operator and the stack is empty or contains a left parenthesis on top, push the incoming operator onto the stack.

5.If the incoming symbol is an operator and has either higher precedence than the operator on the top of the stack, or has the same precedence as the operator on the top of the stack and is right associative -- push it on the stack.

6.If the incoming symbol is an operator and has either lower precedence than the operator on the top of the stack, or has the same precedence as the operator on the top of the stack and is left associative -- continue to pop the stack until this is not true. Then, push the incoming operator.

7.At the end of the expression, pop and print all operators on the stack. (No parentheses should remain.)

Video Representation of the Shunting Yard Algorithm physically.Some words in this video relate to operating systems which we studied last semester.

https://www.youtube.com/watch?v=Wz85Hiwi5MY

*Thompsons Construction*

Also known as  the McNaughton-Yamada-Thompson algorithm. Credited to Ken Thompson. (https://en.wikipedia.org/wiki/Thompson%27s_construction)

This algorithm is a method used to convert or transform a regular expression to an nondeterministic finite automaton(NFA).
This NFA can be used to match strings against the regular expression.

Rules for Thompsons Construction (detailed images) http://www.cs.may.ie/staff/jpower/Courses/Previous/parsing/node5.html

Nondetermnistic Fnite Automation - NFAs are used in the implementation of regular expressions. 
An NFA, consumes a string of input symbols. For each input symbol, it transitions to a new state until all input symbols have been consumed. The notion of accepting an input is similar to that for the DFA. When the last input symbol is consumed, the NFA accepts if and only if there is some set of transitions that will take it to an accepting state. Equivalently, it rejects, if, no matter what transitions are applied, it would not end in an accepting state.
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton

*Overview*

For this project i used Visual Studio Code to code the Shunting Yard Algorithm and Thompsons Construction in python language.
I used cmder to run my code. I recommend both technologies if you wish to pursue a python program.
In this project i began with the shunting yard algorithm and progressed through onto Thompsons Construction where i used the complie function along with a followes function(That returns states that follow the edges/arrows) and a match function(to match string to infix).I then implemented a user input so the user can enter their own infixes and strings. Program runs smoothly in cmder as does the test Shunting Algorithm pythin file. 

