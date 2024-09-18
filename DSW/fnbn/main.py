from itertools import permutations


def find_next_bigger_number(n: int) -> int:
    value = str(n)
    all_comb = sorted(set(([int(''.join(n)) for n in list(permutations(value, len(value)))])))
    max_num_index = all_comb.index(n)
    if max_num_index == len(all_comb) - 1:
        return -1
    return all_comb[max_num_index + 1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(find_next_bigger_number)
