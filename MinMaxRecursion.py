def max(list): #Finds the largest number in the list via recursion
    if len(list) == 1: #Base case
        return list[0]
    else:
        m = max(list[1:]) #Recursion
        return m if m > list[0] else list[0]
    
def min(list): #Finds the smallest number in the list via recursion
    if len(list) == 1: #Base case
        return list[0]
    else:
        m = min(list[1:]) #recursion
        return m if m < list[0] else list[0]

def main():
    list = eval(input("Please enter a comma deliminated list of numbers: "))
    print("Maximum Value: {} ".format(max(list)))
    print("Minimum Value: {}".format(min(list)))

main()