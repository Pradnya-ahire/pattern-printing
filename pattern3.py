for i in range(0,5):      #this for loop used to print 5 rows 
    for j in range(0,5-i):    # This loop prints stars decreasing by 1 in each row
        print("*",end = " ")            # This prints a star with a space after it

    print()     # This moves to the next line after each row
