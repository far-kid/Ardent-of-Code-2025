from day1_part2 import calculate_vector

def right_val(vector, lock_pos):
    zero_count = 0

    def right_add():
        nonlocal lock_pos, zero_count
        lock_pos += vector
        if lock_pos >= 100:
            lock_pos %= 100
            zero_count += 1

    if vector < 100:
        right_add()
    else:
        zero_count += vector // 100
        vector %= 100
        right_add()

    return zero_count, lock_pos

def left_val(vector , lock_pos):
    # zero_count=0
    
    # def left_add():
    #     nonlocal vector , lock_pos , zero_count
    #     lock_pos+=vector
    #     if lock_pos <= 0:
    #         zero_count+=1
    #         print("left add" + str(zero_count))
    #         lock_pos %=100
    
    # if vector > -100:
    #     # if lock_pos + vector <= 0:
    #     #     zero_count+=1
    #     #     lock_pos = (lock_pos + vector) % 100
    #     #     print("Left, first " + str(zero_count))
    #     # else:
    #     #     left_add()
    #     left_add()
        
        
    # else:
    #     zero_count += abs(vector)//100
    #     print("LEFT nonadd")
    #     remainder= (abs(vector)%100)
        
    #     if remainder==0:
    #         vector=0
    #     else:
    #         vector= -remainder
    #         left_add()
    
    if vector == 0:
        return 0, lock_pos  # no movement

    
    d = -vector

    # new position after moving left d steps
    new_pos = (lock_pos - d) % 100

    # smallest step t (1..d) at which we encounter position 0:
    # - if lock_pos > 0, first_t = lock_pos
    # - if lock_pos == 0, the first time we encounter 0 is at t = 100 (full circle)
    first_t = lock_pos if lock_pos > 0 else 100

    if d < first_t:
        zero_count = 0
    else:
        zero_count = 1 + (d - first_t) // 100

    return zero_count, new_pos




def main():
    commands = []
    with open("F:\Ardent-of-Code-2025\Day1\input.txt") as f:
        for line in f:
            clean= line.rstrip('\n')
            commands.append(clean)
    # print(commands)
    value = 50
    zero_count= 0
    
    for comm in commands:
        v = calculate_vector(com=comm)
        if v<0:
            ans = left_val(v , value)
            zero_count+=ans[0]
            value=ans[1]
        else:
            ans = right_val(v , value)
            zero_count+=ans[0]
            value=ans[1]
            
    print(zero_count)
    
if __name__ =="__main__":
    main()
            
    
    