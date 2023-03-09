import re
from fractions import Fraction
def get_input():
    allocate_pattern = '(^ALLOT_WATER (2|3) (\d+:\d+))'
    test_string = input()
    result = re.match(allocate_pattern, test_string)
    if(not result):
        print('Value provided maybe incorrect, plese check the format and reenter')
        getInput()
    else:
        values = {
            'flat_type': result.groups()[1],
            'ratio': result.groups()[2],
            'guests': 0
        }

        while True:
            nextValues = input()
            if ('ADD_GUESTS' in nextValues):
                add_value = int(nextValues.split(' ')[-1])
                if(add_value < 0):
                    print('Removing guests is not allowed')
                else:
                    values['guests'] = values['guests']+ (add_value if add_value>0 else 0)
            elif('BILL' in nextValues):
                return values;
            else:
                print('ADD_GUESTS or BILL commands only')
def get_required_water(input):
    people = 3 if input['flat_type'] == '2' else 5
    guests = input['guests']
    return {
        'allotted_amount': people*10*30,
        'required_amount':(people+guests)*10*30
    }
def calculate_bill(amount, ratio):
    normal_bill = get_normal_bill(amount['allotted_amount'], ratio)
    tanker_bill = get_tanker_bill(amount['required_amount']-amount['allotted_amount'])
    print(normal_bill, tanker_bill)
    return normal_bill+tanker_bill

def get_normal_bill(liters, ratio):
    temp = ratio.split(':')
    ratio = Fraction(int(temp[0]), int(temp[1])+int(temp[0]))
    amount = int(liters * ratio + liters*(1-ratio)*1.5)
    print(ratio, liters, amount)
    return amount

def get_tanker_bill(liters):
    print(liters,'tanker')
    price_brackets = [1500,1000,500]
    prices = [5,3,2] #anything else will be 8
    total = 0
    while(True):
        bracket = price_brackets.pop()
        if(liters-bracket > 0):
            total += bracket*prices.pop()
            liters -= bracket;
        else:
            total +=liters*prices.pop()
            liters = 0
            break
    if liters:
        total += liters*8
    return total
def main():
    input_values = get_input()
    amount = get_required_water(input_values)
    print(input_values, amount["required_amount"], amount["allotted_amount"])
    bill = calculate_bill(amount, input_values['ratio'])
    print(amount["required_amount"], bill)
     
main()
# get inputs from user
# content = []
# while True:
#     # get allot input, it must be the first one 
#     allotedValue = input();
#     print(allotedValue)
#     break;
# # while True:
# #     try:
# #         val = input()
# #         print(val)
# #     except EOFError:
# #         break
# #     content.append(val)
# # print(content)
