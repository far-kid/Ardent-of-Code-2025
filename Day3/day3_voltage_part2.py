def findmax(bank)->int:
    ##BruteForce approach
    maxsum = 0

    output = []
    start_index = 0
    length = len(bank)
    for index in range(12)[::-1]:
        max_value = max(bank[start_index:length-index])
        start_index = bank[start_index:length-index].index(max_value)+start_index+1
        output.append(max_value)
    return int(''.join(str(num) for num in output))
 
                


def main():
    powerbanks =[]
    with open("F:\Ardent-of-Code-2025\Day3\input.txt") as f:
        powerbanks = f.read().splitlines()
    
    max_sum = 0
    for i in range(len(powerbanks)):
        max_sum += findmax(powerbanks[i])
    
    print(max_sum)
        
    
    
    
if __name__ == "__main__":
    main()