def isPrimeNum(num):
    '''
    Проверка, является ли число простым.
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'не является простым числом')
            break
    else:
        print(num,'является простым числом')
        
isPrimeNum(24)