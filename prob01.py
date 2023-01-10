import numpy as np

def dfdx(x,y):
    return 10*x*y

def main():
    print(dfdx(2,3))

if __name__ == "__main__":
    main()