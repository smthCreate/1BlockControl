def sort_len(data_ls):
    for i in data_ls:
        if len(i) > 3:
            data_ls.pop(data_ls.index(i))
    return data_ls

new_data = [i for i in input().split()]
print(sort_len(new_data))
