import re


def cal(s):
    s = re.sub(r"[\[\{]", "(", s)
    s = re.sub(r"[\]\}]", ")", s).replace(" ", "")
    stack = []

    for x in re.split(r"(\D)", s):
        if not x:
            continue
        if x == ")":
            sub_stack = []
            while stack:
                y = stack.pop()
                if y == "(":
                    break
                sub_stack.append(y)
            result = cal_without_parentheses(sub_stack)
            stack.append(result)
        else:
            stack.append(x)

    return cal_without_parentheses(stack[::-1])


def cal_without_parentheses(stack):
    sub_stack = []
    while stack:
        x = stack.pop()
        if x == "*":
            r = float(sub_stack.pop()) * float(stack.pop())
            sub_stack.append(r)
        elif x == "/":
            r = float(sub_stack.pop()) / float(stack.pop())
            sub_stack.append(r)
        else:
            sub_stack.append(x)

    result = 0
    while sub_stack:
        x = sub_stack.pop(0)
        if x == "+":
            result += float(sub_stack.pop(0))
        elif x == "-":
            result -= float(sub_stack.pop(0))
        else:
            result = float(x)

    return result


def main(args):
    print(cal(args[0]))
