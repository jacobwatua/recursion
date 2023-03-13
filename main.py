arg = "Jacob Watua"
def rev_string (s):
    def rev (t = len(s)):
        if t == 0:
            print()
            return
        print(arg[t - 1], end="")
        t -= 1
        rev (t)
    return rev()

c = lambda s : rev_string(s)

c((arg))