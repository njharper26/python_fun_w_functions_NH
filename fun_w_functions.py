def odd_even(start, end):
    for num in range(start, end):
        if num % 2 != 0:
            print "Number is " + str(num) + "." + "This is an odd Number"
        else:
            print "Number is " + str(num) + "." + "This is an even Number"
        
result = odd_even(1, 2001)
print result

def lst_multipler(lst, mult):
    for i in range(0, len(lst)):
        lst[i] *= mult
    return lst

lst = [2,4,10,16]
mult = 5

result = lst_multipler(lst, mult)
print result
            
def lst_multipler(lst, mult):
    for i in range(0, len(lst)):
        lst[i] *= mult
    return lst   

def layered_multiples(lst):
    outer_lst = []
    for num in lst:
        inner_lst = []
        for x in range(0, num):
            inner_lst.append(1)
        outer_lst.append(inner_lst)
    return outer_lst

lst_1 = [2,4,5]
mult = 3
result = layered_multiples(lst_multipler(lst_1, mult))
print result