def getSum(x,y):
    try:
        sum = x+y
        print('Sum is : ' + str(sum))
        return sum
    except Exception as e:
        print(e)
        print("Error occuren in run time")
        return -100
    
