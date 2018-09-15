#USE OF ABS
# --Return the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its
#magnitude is returned.
# SYNTAX -- abs(x)
def ABS():
    a=float(input("enter anytype of number - positive , negative , neutral , floating point ,etc"))
    b=abs(a)
    print("The abs(absolut value) of your input number {} is {}".format(a,b))
    c=complex(input("enter the complex number"))
    d=abs(c)
    print("The abs(absolut value) of your input number {} is {}".format(c,d))
    return b,d
ABS()




#USE OF ALL
# -- Return True if all elements of the iterable are true (or if the iterable is empty)
#SYNTAX -- all(iterable)
#iterable are that can have index , that can be kept in loop

def ALL():
    a = input("enter iterables (non integer values) ")
    try:
        a = eval(a)
        print(a, type(a), all(a))
    except:
        print(a, type(a), all(a))

    return a
ALL()





#USE OF ANY
#-- Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
#SYNTAX -- any(iterable)
#somewhat opposite of all(Like AND and OR )
def ANY():
    a = input("enter iterables (non integer values) ")
    try:
        a = eval(a)
        print(a, type(a), any(a))
    except:
        print(a, type(a), any(a))

    return a
ANY()




#USE OF ASCII
# SYNTAX --ascii(object)

