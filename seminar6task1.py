# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
s = '1 + 2 * 3 / 6'
lst = s.split()
while len(lst) > 1:
    while '*' in lst or '/' in lst:
        if lst.count('*') > 0 and lst.count('/') > 0:
            if lst.index('/') > lst.index('*'):
                lst[lst.index('*') - 1] = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
                lst.pop(lst.index('*') + 1)
                lst.pop(lst.index('*'))
            else:
                lst[lst.index('/') - 1] = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
                lst.pop(lst.index('/') + 1)
                lst.pop(lst.index('/'))
        else:
            if '*' in lst:
                lst[lst.index('*') - 1] = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
                lst.pop(lst.index('*') + 1)
                lst.pop(lst.index('*'))
            else:
                lst[lst.index('/') - 1] = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
                lst.pop(lst.index('/') + 1)
                lst.pop(lst.index('/'))
    else:
        while '+' in lst or '-' in lst:
            if lst.count('+') > 0 and lst.count('-') > 0:
                if lst.index('-') > lst.index('+'):
                    lst[lst.index('+') - 1] = int(lst[lst.index('+') - 1]) + int(lst[lst.index('+') + 1])
                    lst.pop(lst.index('+') + 1)
                    lst.pop(lst.index('+'))
                else:
                    lst[lst.index('-') - 1] = int(lst[lst.index('-') - 1]) - int(lst[lst.index('-') + 1])
                    lst.pop(lst.index('-') + 1)
                    lst.pop(lst.index('-'))
            else:
                if '+' in lst:
                    lst[lst.index('+') - 1] = int(lst[lst.index('+') - 1]) + int(lst[lst.index('+') + 1])
                    lst.pop(lst.index('+') + 1)
                    lst.pop(lst.index('+'))
                else:
                    lst[lst.index('-') - 1] = int(lst[lst.index('-') - 1]) / int(lst[lst.index('-') + 1])
                    lst.pop(lst.index('-') + 1)
                    lst.pop(lst.index('-'))

print(s, '=', lst[0])

