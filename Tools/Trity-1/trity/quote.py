# coding: utf-8
#!/usr/bin/env python
from random import *
def quote():
    joke1 = "A lot of hacking is playing with other people, you know, getting them to do strange things."
    joke2 = "When solving problems, dig at the roots instead of just hacking at the leaves."
    joke3 = "Most hackers are young because young people tend to be adaptable. As long as you remain adaptable, you can always be a good hacker."
    joke4 = "Hacking is fun if you're a Hacker"
    joke5 = "Behind every successful Coder there an even more successful De-coder to understand that code"
    joke6 = "Hacking just means building something quickly or testing the boundaries of what can be done"
    joke7 = "Hackers are not crackers"
    joke8 = "If you give a hacker a new toy, the first thing he'll do is take it apart to figure out how it works."
    joke9 = "Press any key... no, no, no, NOT THAT ONE!"
    headers = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9]
    print headers[randint(0,8)]

