invalid_sum = 0

def calculate(lower:int , upper:int ):
    global invalid_sum
    # print(lower, upper)
    for i in range(lower , upper+1):
        if(invalid_num(i)):
            invalid_sum+=i
            
    return
    
    
def invalid_num(num:int)->bool:
    res = list(map(int, str(num)))
    len_list = len(res)
    # if len_list%2!=0:
    #     return False
    l , r = 0 , len_list//2
    while (r<len_list):
        if res[l]!=res[r]:
            return False
        l+=1
        r+=1
    print("Invalid number" ,num)
    return True
        



def main():
    list_id= []
   
    with open("F:\Ardent-of-Code-2025\Day2\input.txt") as f:
        line = f.read().strip()
        list_id = line.split(",")

    for list_item in list_id:
        # print(list_item)
        lower, upper = list_item.split("-")
        lower, upper = int(lower) , int(upper)
        calculate(lower=lower, upper=upper)
    
    print(invalid_sum)

if __name__=="__main__":
    main()