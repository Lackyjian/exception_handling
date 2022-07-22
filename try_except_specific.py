def fun(a):
    if a < 4:
        a  = a/(a-3)
    print("Value of a = ", a)
      
try:
    fun(3)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")