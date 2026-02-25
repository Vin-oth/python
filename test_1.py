def section_a():
    n = int(input())
    print("Even" if n % 2 == 0 else "Odd")

    marks = int(input())
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 60:
        print("C")
    elif marks >= 50:
        print("D")
    else:
        print("F")

    num = int(input())
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

    a = int(input())
    b = int(input())
    c = int(input())
    print(min(a, b, c))

    pwd = input()
    print("Valid Password" if pwd == "Python123" else "Invalid Password")

    x = float(input())
    y = float(input())
    op = input()
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
    else:
        print("Invalid Operator")

    age = int(input())
    print("Eligible" if age >= 18 else "Not Eligible")

    ch = input()
    if ch.lower() in "aeiou":
        print("Vowel")
    elif ch.isalpha():
        print("Consonant")
    else:
        print("Other")

    day = input().lower()
    if day in ["saturday", "sunday"]:
        print("Weekend")
    else:
        print("Weekday")


def section_b():
    l = [1, 22, 3, 44, 55, 6, 11, 1200]
    l.insert(5, 4)
    l.remove(44)
    l.append(88)
    l.pop(1)
    m = [1, 2, 3, 546]
    l.extend(m)
    print(l)


def section_c():
    s = "HelloWorld"
    s = s[:5] + "Python" + s[5:]
    s = s.replace("World", "")
    s = s + "2024"
    s = s[0] + s[2:]
    t = "Programming"
    s = s + t
    print(s)


def section_d():
    marks = int(input())
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 50:
        print("Grade D")
    else:
        print("Grade F")

    ch = input()
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

    username = input()
    password = input()
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Login Failed")


if __name__ == "__main__":
    section_a()
    section_b()
    section_c()
    section_d()