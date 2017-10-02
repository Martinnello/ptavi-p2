# /usr/bin/python3

import sys
import calcoo


class CalculadoraHija (calcoo.Calculadora):

    def mul(self):
        return self.Num1 * self.Num2

    def div(self):
        return self.Num1 / self.Num2

if __name__ == "__main__":

    try:

        Num1 = float(sys.argv[1])
        Num2 = float(sys.argv[3])

    except ValueError:
        sys.exit("   Non numerical parameters")
    except IndexError:
        sys.exit("   Try ->   Num1   suma/resta/multiplica/divide   Num2")

    Opr = sys.argv[2]
    CH = CalculadoraHija(Num1, Num2)

    if Opr == "suma":
        Res = CH.suma()
    elif Opr == "resta":
        Res = CH.resta()
    elif Opr == "multiplica":
        Res = CH.mul()
    elif Opr == "divide":
        if Num2 == 0:
            sys.exit("Division by zero is not allowed")
        else:
            Res = CH.div()
    else:
        sys.exit("   Try ->   Num1   suma/resta/multiplica/divide   Num2")

    print(Res)
