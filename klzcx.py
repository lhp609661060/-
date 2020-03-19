#coding=utf8

"""
考拉兹猜想 （奇偶归一猜想）
"""

import sys

def main(data):
    _l = []

    def klzcx(n):
        _l.append(n)
        if n == 1:
            return 1

        if n % 2 == 0:
            return klzcx(n//2)

        return klzcx(3*n+1)

    klzcx(int(data))
    print('result', _l)
    print('length', len(_l))
    print('max', max(_l))
    print('avg', sum(_l)/len(_l))

if __name__ == '__main__':
    main(sys.argv[1])
