import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

if not args.type:
    print('Incorrect parameters')

m = 1  # month counter

if args.type == 'diff':
    if not (args.principal and args.periods and args.interest):
        print('Incorrect parameters')
    else:
        summa = 0
        while m <= args.periods:
            nom_int_rate = args.interest / 1200
            diff_payment = math.ceil(args.principal / args.periods + nom_int_rate *
                                     (args.principal - (args.principal * (m - 1)) / args.periods))
            summa += diff_payment
            print(f'Month {m}: payment is {diff_payment}')
            m += 1
        overpayment = math.ceil(summa - args.principal)
        print()
        print(f'Overpayment = {overpayment}')

if args.type == 'annuity':
    if not args.periods:
        if not (args.principal and args.payment and args.interest):
            print('Incorrect parameters')
        else:
            nom_int_rate = args.interest / 1200
            periods = math.ceil(math.log(args.payment / (args.payment - nom_int_rate * args.principal),
                                         1 + nom_int_rate))
            overpayment = math.ceil(args.payment * periods - args.principal)
            if periods >= 12:
                if periods // 12 == 1:
                    print(f'It will take {periods} year to repay this loan!')
                    print(f'Overpayment = {overpayment}')
                elif periods % 12 == 0:
                    print(f'It will take {periods // 12} years to repay this loan!')
                    print(f'Overpayment = {overpayment}')
                else:
                    print(f'It will take {periods // 12} years and {periods % 12} months to'
                          f'repay this loan!')
                    print(f'Overpayment = {overpayment}')
            if periods < 12:
                print(f'It will take {periods} months to repay this loan!')
                print(f'Overpayment = {overpayment}')
            if periods == 1:
                print(f'It will take {periods} month to repay the loan!')
                print(f'Overpayment = {overpayment}')
    if not args.principal:
        if not (args.periods and args.payment and args.interest):
            print('Incorrect parameters')
        else:
            nom_int_rate = args.interest / 1200
            loan_principal = math.floor(args.payment / (((nom_int_rate * (1 + nom_int_rate) ** args.periods) /
                                                        ((1 + nom_int_rate) ** args.periods - 1))))
            print(f'Your loan principal = {loan_principal}!')
            overpayment = math.floor(args.payment * args.periods - loan_principal)
            print(f'Overpayment = {overpayment}')
    if not args.payment:
        if not (args.periods and args.principal and args.interest):
            print('Incorrect parameters')
        nom_int_rate = args.interest / 1200
        annuity = math.ceil((args.principal * nom_int_rate * (1 + nom_int_rate) ** args.periods) /
                            ((1 + nom_int_rate) ** args.periods - 1))
        print(f'Your annuity payment = {annuity}!')
        overpayment = math.floor(annuity * args.periods - args.principal)
        print(f'Overpayment = {overpayment}')
