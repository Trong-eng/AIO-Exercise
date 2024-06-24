def check_int(value):#check the value ìf it is an integer
    try:
        int(value)
        return True
    except ValueError:
        return False
def check_greaterthanzero(value):# check the value if it is greater than zero
    if value > 0:
        return True
    else:
        return False
def condition(name, value):#check the value if it is satisfied that is int and > 0
    if check_int(value):
        value = int(value)
        if check_greaterthanzero(value):
            return value
        else:
            print(f'{name} must be greater than zero')
            return None
    else:
        print(f'{name} must be an integer')
        return None
tp = input("Enter tp: ")
fp = input("Enter fp: ")
fn = input("Enter fn: ")
tp = condition('tp', tp)
fp = condition('fp', fp)
fn = condition('fn', fn)
if type(tp) is int and type(fp) is int and type(fn) is int and tp > 0 and fn > 0 and fp > 0:#check if it is satisfied all conditions
    precision = tp / (tp+fp)
    print('precision is',precision)
    recall = tp / (tp+fn)
    print('recall is',recall)
    f1_score = 2 * ((precision * recall)/(precision + recall))
    print('f1-score is',f1_score)






    

