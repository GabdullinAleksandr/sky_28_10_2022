
def decor_int(func):
    def inner(*args):
        try:
            res = func(args[0], int(args[1]))
            return res
        except:
            numb = {
                'один': 1,
                'два': 2,
                'три': 3,
                'четыре': 4,
                'пять': 5,
            }
            if args[1] in numb.keys():
                res = func(args[0], numb[args[1]])
                return res
            elif type(args[1]) is tuple:
                raise TypeError("unsupported operand type(s) for +: 'Int' and 'tuple'")
            else:
                raise TypeError('справа от знака "+" непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.')
    return inner


class Int(int):
    @decor_int
    def __add__(self, other):
        return super().__add__(other)


x = Int(5)
print(x.__add__('5'))
