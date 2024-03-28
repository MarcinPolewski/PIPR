def calculate_avg(input_array):
    input_sum = 0
    for element in input_array:
        input_sum += int(element)
    return input_sum / len(input_array)


def count_elements_above_average(input_array):
    """
    returns number of such elements, we
    do not verify correctness of imput
    """
    counter = 0
    input_avg = calculate_avg(input_array)

    for element in input_array:
        element = int(element)
        if element > input_avg:
            counter += 1
    return counter


def count_elements_for_arrays(input_arrays):
    answer = []
    for array in input_arrays:
        try:
            answer.append(count_elements_above_average(array))
        except ValueError:
            answer.append("ZŁA WARTOŚĆ")
        except ZeroDivisionError:
            answer.append("DZIELENIE PRZEZ ZERO")
        # except:
        #     answer.append("dupa")

    return answer


# co z fload? zakładamy e to złe wejście
