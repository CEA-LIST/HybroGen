# RPN compilation

This compilette example implements an evalation of an expression
written in RPN (Reverse Polish Notation)

https://en.wikipedia.org/wiki/Reverse_Polish_notation

## Demonstration

The demonstration shows a temperature conversion between Fahrenheit
and Celcius

Those function calls generate two function which compare from one

```C
        pifi c2f = rpn_compile("9*5/32+");
        pifi f2c = rpn_compile("32-5*9/");
'''

## Expression evaluation

This demonstration could be used as a compiler for any RPN expression.