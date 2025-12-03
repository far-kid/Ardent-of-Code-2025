def findmax_brut(number)->int:
    ##BruteForce approach
    maxsum = 0
    for i in range(len(number)):
        for j in range(i , len(number)):
            if i==j:
                continue
            else:
                maxsum = max(maxsum , int(number[i]+number[j]))
    print(maxsum)
    return maxsum


def main():
    powerbanks =[]
    with open("F:\Ardent-of-Code-2025\Day3\input.txt") as f:
        powerbanks = f.read().splitlines()
    
    max_sum = 0
    for i in range(len(powerbanks)):
        max_sum += findmax_brut(powerbanks[i])
    
    print(max_sum)
        
    
    
    
if __name__ == "__main__":
    main()