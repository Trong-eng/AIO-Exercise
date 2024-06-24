import random#use the module random to pick a number
number_samples = input()
function = input()
def loss_function(n):
    if number_samples.isnumeric():#check if it is integer|
        s = 0
        k = 0
        for i in range(int(number_samples)):
                target = random.uniform(0,10)
                predict = random.uniform(0,10)
                if function == 'MAE':
                    k+=1  #k have a mission is that count to n
                    s += abs(target-predict)
                    print(function,end=' ')
                    print('sample',i,end=' ')
                    print('target :',target,end=' ')
                    print('predict :',predict,end=' ')
                    if k == int(number_samples) :#count when k == n so we can divide the the formula to number of samples
                        s /= k
                    print('loss:',s)
                elif function == 'MSE':
                    k+=1
                    s += (target - predict)**2
                    print(function,end=' ')
                    print('sample',i,end=' ')
                    print('target :',target,end=' ')
                    print('predict :',predict,end=' ')
                    if k == int(number_samples) :
                        s /= k
                    print('loss:',s)
    else:
        print('number of samples must be an integer number')
loss_function(number_samples)

            
