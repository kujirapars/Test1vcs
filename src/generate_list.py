import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    sum = 0
    for i in alist:
        sum += alist[i]
    assert (alist != []),"List is empty"
    assert (sum >= 0),"Sum's list is less than 0"
    return alist
    
def printIt():
    print( generate_list() )
    
def main()
    printIt()
    
if __name__ == '__main__':
    print("Test printIt():")
    main()
