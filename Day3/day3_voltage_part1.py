def findmax(number)->int:
    pass
        


def main():
    powerbanks =[]
    with open("F:\Ardent-of-Code-2025\Day3\input_sample.txt") as f:
        powerbanks = f.read().splitlines()
    
    max_sum = 0
    for i in range(len(powerbanks)):
        max_sum += findmax(powerbanks[i])
    
    print(max_sum)
        
    
    
    
if __name__ == "__main__":
    main()