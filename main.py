def sum_even_index_mult_last(lst):
    if not lst:
        return 0


    sum_even_indices = sum(lst[i] for i in range(0, len(lst), 2))


    last_element = lst[-1]


    result = sum_even_indices * last_element

    return result



my_list = [2, 3, 5, 9, 6]
result = sum_even_index_mult_last(my_list)
print(result)