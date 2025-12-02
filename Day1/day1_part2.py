##HORRIBLE CODE_ USE DAY!_ALt

def calculate_vector(com :str)->int:
    quantity = int(com[1:])
    if com[0]=="R":
        return quantity
    else:
        return -quantity
    
def vector_actual(vector_val)->int:
    return (vector_val%100)

def get_result(com :str)->int:
    return vector_actual(calculate_vector(com))

def count_zeros_in_a_vector(quantity)->int:
    value = abs(quantity)
    return value//100


def do_it_left(value, vector):
    count_zero=0
    if vector<0: ## LEFT CASE
        if vector > -100:  ##WHEN 
            if value > abs(vector):
                value+=vector
            else:
                count_zero+=1
                print("left,  v<0 v> -100: " + str(vector))
                value+=vector
                value%=100
        else:
            while vector < -100:
                print("left,  v<0 v<  -100: " + str(vector))                
                count_zero+=1
                vector+=100
                if vector>=100:
                    count_zero+=1
                    vector=vector%100
            if value > abs(vector):
                value+=vector
            else:
                count_zero+=1
                print("left,  v<0 v else: " + str(vector))                   
                value+=vector
                vector%=100
    print(value)
    if value>=100 or value<=-100:
        value%=100
        count_zero+=1
    return [count_zero , value]


def do_it_right(value, vector):
    count_zero=0
    if vector>0: 
        if vector <= 100:  
            if value > abs(vector):
                value+=vector
                if value>=100:
                    count_zero+=1
                    value%=100
            else:
                count_zero+=1
                print("right , v>0 v<100: " + str(vector))
                value+=vector
                vector%=100
        else:
            while vector > 100:
                count_zero+=1
                vector-=100
                print("right ,loop ,  v>0 v>100: " + str(vector))
            if value > abs(vector):
                value+=vector
            else:
                print("right ,loop ,  v>0 else: " + str(vector))
                count_zero+=1
                value+=vector
                vector%=100
    if value>=100 or value<=-100:
        value%=100
        count_zero+=1
    return [count_zero , value]



def do_it_one_at_a_time(value, vector):
    flag = True
    count_zero = 0
    if vector>0:
        out = do_it_right(value=value, vector=vector)
        count_zero+=out[0]
        value = out[1]
    elif vector==0:
        pass
    else:
        out = do_it_left(value=value, vector=vector)
        count_zero+=out[0]
        value = out[1]
        
    return [count_zero, value]
    

def main():
    commands = []
    with open("F:\Ardent-of-Code-2025\Day1\input.txt") as f:
        for line in f:
            clean= line.rstrip('\n')
            commands.append(clean)
    print(commands)
    value = 50
    zero_count= 0
    for com in commands:
        print()
        print(com)
        print()
        # value+=get_result(com=com)
        # value%=100
        # zero_count+=count_zeros_in_a_vector(calculate_vector(com=com))
        # if value==0:
        #     zero_count+=1
        ans=do_it_one_at_a_time(value=value ,vector=calculate_vector(com=com))
        value = ans[1]
        zero_count+=ans[0]
        print("FINAL VALUE=="+str(value))
    print(zero_count)
    
if __name__ == "__main__":
    main()