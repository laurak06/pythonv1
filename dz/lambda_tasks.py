operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    }

def main():
    while True:
        print('Calculator')
        try:
            operator = input('enter operation(# if want to quit): ')
            if operator == '#':
                break
            num1 = float(input('enter 1 number: '))
            num2 = float(input('enter 2 number: '))
            if operator == '+':
                print(operators['+'](num1, num2))
            elif operator == '-':
                print(operators['-'](num1, num2))
            elif operator == '*':
                print(operators['*'](num1, num2))
            elif operator == '/':
                print(operators['/'](num1, num2))
            else:
                print('Такого оператора нет!')
        except ValueError:
            print('only umbers!')
        except ZeroDivisionError:
                print('no zero division!')

        

main()
