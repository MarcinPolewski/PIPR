def fibonacci(predecessor1, predecessor2, current_index):
    # print(predecessor1) #prints fibonacci sequence
    if current_index == 5:
        return predecessor1
    return fibonacci(predecessor2, predecessor1+predecessor2, current_index+1)


print(fibonacci(0, 1, 1))
