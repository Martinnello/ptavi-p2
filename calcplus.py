# /usr/bin/python3

import sys
import csv
import calcoohija


if len(sys.argv) != 2:
    sys.exit("  Try ->  python3 calcplusplus.py < File_Name >")

else:
                #  Vemos si existe el fichero
    try:
        File = sys.argv[1]
        Fich = open(File)
        Fich.close()
    except FileNotFoundError:
        sys.exit("  Try ->  python3 calcplusplus.py < File_Name >")

    #  Abrimos el fichero y lo leemos

    with open(File) as csvfile:

        Reader = csv.reader(csvfile)

        for Row in Reader:

            try:
                Count = float(Row[1])
            except ValueError:
                sys.exit("   Non numerical parameters")  # Operando no es nª

            for Num in Row[2:]:
                try:
                    Num2 = float(Num)
                except ValueError:
                    sys.exit("   Non numerical parameters")	 # El resto

                Opr = Row[0]
                CH = calcoohija.CalculadoraHija(Count, Num2)

                #  Usamos la CalculadoraHija

                if Opr == "suma":
                    Count = CH.suma()
                elif Opr == "resta":
                    Count = CH.resta()
                elif Opr == "multiplica":
                    Count = CH.mul()
                elif Opr == "divide":
                    if Num2 == 0:
                        sys.exit("Division by zero is not allowed")
                    else:
                        Count = CH.div()
                else:
                    sys.exit("Try -> suma/resta/multiplica/divide,Num1,Num2..")

            print(Count)
