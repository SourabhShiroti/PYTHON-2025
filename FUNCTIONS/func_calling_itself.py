def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum

def cal_diff(a=50,b=20):
    diff=a-b
    print(diff)
    return diff

def cal_prod(a,b):
    prod=a*b
    print(prod)
    return prod

def cal_avg(a,b,c,d,e):
    avg=(a+b+c+d+e)/5
    # print(avg)
    return avg

#Function Calling itself

cal_sum(52,68)
cal_diff()
cal_prod(12,34)
print(cal_avg(12,34,56,78,90))