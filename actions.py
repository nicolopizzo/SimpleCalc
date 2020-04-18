from PyQt5.QtWidgets import QLineEdit

def onClick(s, form):
    if isinstance(form, QLineEdit):
        t = form.text()
        form.setText(t + s)
        form.setFocus()

def onClickCalc(form, label):
    res = str(evaluate(form.text()))
    label.setText(form.text())
    form.setText(res)
    form.setFocus()

def onClickDelete(form):
    form.setText("")
    form.setFocus()

def evaluate(s):
    numStack = []
    opStack = []
    operators = ["+", "-", "*", "/", "(", ")"]

    word = ""
    for ch in s:
        if ch not in operators:
            word += ch
        else:
            try:
                if word != "":
                    numStack.append(float(word))
                word = ""
                if ch == ")":
                    x = numStack.pop()
                    y = numStack.pop()
                    numStack.append(__evaluate(opStack.pop(), x, y))

                elif ch == "(":
                    pass

                else:
                    opStack.append(ch)

            except ValueError:
                print("Error") # Debug only
                openErrorDialog("You entered something wrong.")
                return ""

    return numStack.pop()

def openErrorDialog(msg):
    pass

def __evaluate(op, x, y):
    if op == "+":
        return x + y
    
    elif op == "-":
        return y - x

    elif op == "*":
        return x * y

    elif op == "/":
        return y/x
    
    raise ValueError