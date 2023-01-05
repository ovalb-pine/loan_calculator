import math  # importing needed modules
import argparse

parser = argparse.ArgumentParser()  # creating the parser

parser.add_argument('--type', choices=['annuity', 'diff'])  # adding the arguments
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)

args = parser.parse_args()  # parsing the arguments

if not args.type:  # checking if type is specified
    print('Incorrect parameters')
    
if (args.payment or args.principal or args.periods or args.interest) <= 0:  # checking if any arguments are negative
    print('Incorrect parameters')

m = 1  # setting month counter to 1

if args.type == 'diff':  # continuing if differential calculation is chosen
    if not (args.principal and args.periods and args.interest):  # checking if all needed arguments are present
        print('Incorrect parameters')
    else:
        summa = 0  # introducing the sum variable
        while m <= args.periods:  # running the calculation for all given months
            nom_int_rate = args.interest / 1200
            diff_payment = math.ceil(args.principal / args.periods + nom_int_rate *
                                     (args.principal - (args.principal * (m - 1)) / args.periods))
            summa += diff_payment  # adding all monthly payments
            print(f'Month {m}: payment is {diff_payment}')
            m += 1
        overpayment = math.ceil(summa - args.principal)
        print()
        print(f'Overpayment = {overpayment}')

if args.type == 'annuity':  # continuing if annuity calculation is chosen
    if not args.periods:  # continuing if periods need to be calculated
        if not (args.principal and args.payment and args.interest):  # checking if all needed arguments are present
            print('Incorrect parameters')
        else:
            nom_int_rate = args.interest / 1200
            periods = math.ceil(math.log(args.payment / (args.payment - nom_int_rate * args.principal),
                                         1 + nom_int_rate))
            overpayment = math.ceil(args.payment * periods - args.principal)
            if periods >= 12:  # if there are more than 12 months, convert to years
                if periods // 12 == 1:
                    print(f'It will take {periods} year to repay this loan!')
                    print(f'Overpayment = {overpayment}')
                elif periods % 12 == 0:  # if a whole number of years, write without months
                    print(f'It will take {periods // 12} years to repay this loan!')
                    print(f'Overpayment = {overpayment}')
                else:
                    print(f'It will take {periods // 12} years and {periods % 12} months to'
                          f'repay this loan!')
                    print(f'Overpayment = {overpayment}')
            if periods < 12:
                print(f'It will take {periods} months to repay this loan!')
                print(f'Overpayment = {overpayment}')
            if periods == 1:  # if 1 month, remove the 's' from months
                print(f'It will take {periods} month to repay the loan!')
                print(f'Overpayment = {overpayment}')
                
    if not args.principal:  # continuing if the loan principal needs to be calculated
        if not (args.periods and args.payment and args.interest):  # checking if all needed arguments are present
            print('Incorrect parameters')
        else:
            nom_int_rate = args.interest / 1200
            loan_principal = math.floor(args.payment / (((nom_int_rate * (1 + nom_int_rate) ** args.periods) /
                                                        ((1 + nom_int_rate) ** args.periods - 1))))
            print(f'Your loan principal = {loan_principal}!')
            overpayment = math.floor(args.payment * args.periods - loan_principal)
            print(f'Overpayment = {overpayment}')
            
    if not args.payment:  # continuing if the annuity payment needs to be calculated
        if not (args.periods and args.principal and args.interest):  # checking if all needed arguments are present
            print('Incorrect parameters')
        nom_int_rate = args.interest / 1200
        annuity = math.ceil((args.principal * nom_int_rate * (1 + nom_int_rate) ** args.periods) /
                            ((1 + nom_int_rate) ** args.periods - 1))
        print(f'Your annuity payment = {annuity}!')
        overpayment = math.floor(annuity * args.periods - args.principal)
        print(f'Overpayment = {overpayment}')
