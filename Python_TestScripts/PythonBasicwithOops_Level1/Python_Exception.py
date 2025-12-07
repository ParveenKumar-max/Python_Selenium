# Exception is an event that occurs during the execution of the
# program that disrupts the normal flow of the program

ItemCount = 0

if ItemCount != 2:  # Raise keyword means we intentionally throw the exception.
    #raise Exception("Item count is not matched")
    pass                #which means we again intentionally  pass the case.

assert( ItemCount == 2)     # Assert only fails when your condition is not met.
