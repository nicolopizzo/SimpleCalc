from PyQt5.QtWidgets import QLineEdit
import re
import math

# Defining the information of each operator in a tuple (priority, associativity). left=1, right=0
operators = {
    '(': (-1, 1),
    ')': (-1, 1),
    '+': (1, 1),
    '-': (1, 1),
    '*': (2, 1),
    '/': (2, 1),
    '^': (3, 0)
}

def onClick(s, form):
    if isinstance(form, QLineEdit):
        t = form.text()
        form.setText(t + s)
        form.setFocus()

def onClickCalc(form, label):
    res = str(solve(form.text()))
    label.setText(form.text())
    form.setText(res)
    form.setFocus()

def onClickDelete(form):
    form.setText("")
    form.setFocus()


def __to_rpn(s: str):
    stack = []
    rpn = ""

    for i in range(len(s)):
        if s[i].isspace():
            continue

        elif re.match('[\-\.]?[0-9]', s[i:]):
            rpn += s[i]

        elif s[i] == ')':
            while stack and stack[-1] != '(':
                rpn += ' ' + stack.pop() + ' '
            stack.pop()

        elif s[i] == '(':
            stack.append(s[i])

        elif operators.get(s[i]): #Check to see if the operator exists 
            rpn += ' '
            p_now, a_now = operators[s[i]]
            if stack: p_last, _ = operators[stack[-1]]
            while stack and p_now <= p_last and a_now:
                rpn += stack.pop() + ' '
            stack.append(s[i])

        else:
            raise Exception()

    while stack:
        rpn += ' ' + stack.pop()

    return rpn

def __rpn_solve(s):
    s = s.split()
    stack = []
    for x in s:
        try:
            stack.append(float(x))
        except ValueError: #means it is an operand
            a = stack.pop()
            # Unary operations
            if x == '%':
                stack.append(a/100)
                continue

            b = stack.pop()
            if x == '+':
                stack.append(a+b)
            elif x == '-':
                stack.append(b-a)
            elif x == '*':
                stack.append(a*b)
            elif x == "/":
                stack.append(b/a)
            elif x == '^':
                stack.append(b**a)
    
    return stack.pop()


def solve(s):
    rpn = __to_rpn(s)
    return __rpn_solve(rpn)