def func(n):
    if n == 1:
        print(n)
        return n  # stop recursion
    n -= 1  # decrease value in memory slot
    func(n)  # recursion
    n += 1  # change value in ms back for printing
    print(n)


func(10)
