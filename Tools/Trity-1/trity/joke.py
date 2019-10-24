# coding: utf-8
#!/usr/bin/env python
from random import *
def joke():
    joke1 = "I like telling UDP jokes because I don't care if you don't get them"
    joke2 = "CAPS LOCK - Preventing Login Since 1980."
    joke3 = "In a world without fences and walls, who needs Gates and Windows?"
    joke4 = "If at first you don’t succeed; call it version 1.0."
    joke5 = "Programmers are tools for converting caffeine into code."
    joke6 = "Hacking is like sex. You get in, you get out, and hope that you didn’t leave something that can be traced back to you."
    joke7 = "!false - its funny because its true"
    joke8 = "<joke>Joke Here</joke>"
    joke9 = "Hide&Seek champion - ; - Since 1958"
    headers = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9]
    print headers[randint(0,8)]

