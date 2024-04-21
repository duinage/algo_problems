def sort_bin_array(bin_arr: list) -> list:
    """
    Function sort binary array in linear time without additional memory.
    Example: [0, 1, 1, 0, 0, 1, 1, 0, 1, 0] -> [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].

    Params:
        bin_arr (list): binary array to be sorted.
    Return:
        (list) sorted array.
    """
    bin_arr = list(bin_arr) # to avoid numpy arrays
    final_i = len(bin_arr)
    i = 0
    while i < final_i:
        if bin_arr[i] == 1:
            bin_arr = bin_arr[:i] + bin_arr[i+1:] + [bin_arr[i]]
            final_i -=1
        else:
            i += 1
    return bin_arr


if __name__=="__main__":
    array = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0]
    sorted_array = sort_bin_array(array)
    print(f'{sorted_array=}') # output: sorted_array=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]