if __name__ == '__main__':
    a = int(input("Введите целое число "))
    print(type(a))
    print(1, 2, 3, sep=",")
    print(3.2 // 2)

    s = 4 - 3j
    s_ = s.conjugate()
    print(s_)
    print(abs(s_))

    print(round(3.4), round(3.5), round(3.6))

    print("Число a = %d" % a, end="")
