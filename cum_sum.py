# The cumulative sum of a sequence of numbers is a running total that adds up the elements in the sequence as it progresses. 
# Given a list of numbers, the cumulative sum at each position is computed by adding the sum of all previous numbers
# in the list up to the current position, including the number at the current position itself.


def cumsum(numbers):
    return recursive_cumsum(numbers, index=0, accu=[0])

def recursive_cumsum(numbers, index, accu):
    if index == len(numbers):
        return accu[1:]
    
    accu.append(numbers[index]+accu[-1])
    return recursive_cumsum(numbers, index+1, accu)

if __name__=="__main__":
    example = [4, 6, 12]
    print("The result for [4, 6, 12]: ", cumsum(example))