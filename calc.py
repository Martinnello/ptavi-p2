# /usr/bin/python3

import sys


try:

    Num1 = sys.argv[1]
    Opr = sys.argv[2]
    Num2 = sys.argv[3]

    if Opr == "suma":
        Res = float(Num1) + float(Num2)
    elif Opr == "resta":
        Res = float(Num1) - float(Num2)
    else:
        sys.exit("   Try ->   Num1   suma/resta   Num2")

    print(Res)

except ValueError:
    print("	Non numerical parameters")
except IndexError:
    sys.exit("   Try ->   Num1   suma/resta   Num2")
