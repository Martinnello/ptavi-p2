# /usr/bin/python3

import sys


class Calculadora:

    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2

    def suma(self):
        return self.Num1 + self.Num2

    def resta(self):
        return self.Num1 - self.Num2

if __name__ == "__main__":

    try:

        Num1 = float(sys.argv[1])
        Num2 = float(sys.argv[3])

    except ValueError:
        sys.exit("	Non numerical parameters")
    except IndexError:
        sys.exit("   Try ->   Num1   suma/resta   Num2")

    Opr = sys.argv[2]
    Cal = Calculadora(Num1, Num2)

    if Opr == "suma":
        Res = Cal.suma()
    elif Opr == "resta":
        Res = Cal.resta()
    else:
        sys.exit("   Try ->   Num1   suma/resta   Num2")

    print(Res)
