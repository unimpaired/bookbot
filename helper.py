def quick_sort_lists(the_list: list[tuple[str, int]]):   
    
    if len(the_list) <= 1:
        return the_list
    
    pivot = the_list[-1]
    left = []
    right = []


    for element in the_list[:-1]:
        if element[1] > pivot[1]:
            left.append(element)
        else:
            right.append(element)

    return quick_sort_lists(left) + [pivot] + quick_sort_lists(right)


def format_to_string(sorted_dic: dict[str, int]) -> str:
    line = ''
    dic = sorted_dic.items()
    
    for key, value in dic:
        line += f'{key}: {value}\n'

    return f'{line}'