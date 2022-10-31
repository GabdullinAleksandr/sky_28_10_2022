
class Int(int):
    def __add__(self, other):
        try:
            return super().__add__(int(other))
        except:
            numb = {
                'один': 1,
                'два': 2,
                'три': 3,
                'четыре': 4,
                'пять': 5,
            }
            if other in numb.keys():
                return super().__add__(numb[other])
            elif type(other) is tuple:
                raise TypeError("unsupported operand type(s) for +: 'Int' and 'tuple'")
            else:
                raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')


x = Int(5)
print(x.__add__('два'))
