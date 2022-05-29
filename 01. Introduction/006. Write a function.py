def is_leap(year):

    # Write your logic here
    if (year%100 == 0 and year%400 != 0) or year%4 !=0:
        leap = False
    else:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))