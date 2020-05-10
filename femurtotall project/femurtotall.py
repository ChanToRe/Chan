#femur length를 이용하여 tall을 추정

#Male
def M_pearson(number):
    result = 81.306 + 1.880 * number
    return result

def M_Trotter(number):
    result = 2.15 * number + 72.57
    return result

def M_huzii(number):
    result = (2.47 * (number*10) + 549.01)/10
    return result

#Female
def F_pearson(number):
    result = 72.844 + 1.945 * number
    return result

def F_huzii(number):
    result = (2.24 * (number*10) + 610.43)/10
    return result
