
# 使用 -m timeit模块计算耗时
# python -m timeit '100*100'
# python -m timeit "from test_timeit import factorial" "factorial(20)"

def factorial(n):
    if n == 1:
        return 1
        return n * factorial(n - 1)


if __name__ == "__main__":
    factorial(30)
