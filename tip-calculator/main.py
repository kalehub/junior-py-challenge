# tip calculator

def calculate_tip(tb, pt):
    for item in pt:
        _res = round(((item/100)*tb),2)
        after_tip = round(tb+_res,2)
        print('{}% tip is ${}. which brings your total to ${}'.format(item, _res, after_tip))

def get_total_bill(tb):
    exact_bill = ''
    tb = tb.split('$')
    exact_bill = exact_bill.join(tb)
    return float(exact_bill)

def main():
    poss_tip = (18, 20, 35)
    total_bill = str(input('what\'s the total bill for today, please? : '))
    total_bill = get_total_bill(total_bill)
    calculate_tip(total_bill, poss_tip)

if __name__ == '__main__':
    main()




