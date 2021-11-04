# InputString: Priya
# outputs:
# pRIYA
# R
# AYIRp
def swapcase(s):
    p=s.swapcase()
    print(p)
    print(p[1])
    reverse=p[::1]
    print(reverse)
if __name__ == "__main__":
    s=input()
    swapcase(s)
