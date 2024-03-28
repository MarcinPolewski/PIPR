def check_input(sequence, substring_len):
    if not sequence:
        raise ValueError("provided sequence is empty")
    try:
        substring_len = int(substring_len)
    except Exception:
        raise ValueError("substring cannot be converted to int")

    if substring_len <= 0:
        raise ValueError("Substring value <= 0")

    if substring_len > len(sequence):
        raise ValueError("substring's length greater than sequence's")
    return sequence, substring_len


def find_max_sum(sequence, substring_len):
    sequence, substring_len = check_input(sequence, substring_len)

    current_sum = 0
    max_sum = 0
    max_sum_index = 0  # first number's index

    for element in sequence[:substring_len]:
        current_sum += element
    max_sum = current_sum

    for i in range(0, len(sequence) - substring_len):
        # rozwazamy sume od i do i+substring_len
        current_sum -= sequence[i]
        current_sum += sequence[i + substring_len]

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_index = i + 1

    return max_sum_index, max_sum
