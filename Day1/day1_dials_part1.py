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

def main():
    commands = []
    with open("F:\Ardent-of-Code-2025\Day1\input.txt") as f:
        for line in f:
            clean= line.rstrip('\n')
            commands.append(clean)
    value = 50
    zero_count= 0
    for com in commands:
        value+=get_result(com=com)
        value%=100
        if value==0:
            zero_count+=1
    print(zero_count)
    
if __name__ == "__main__":
    main()