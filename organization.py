def organize_data(final):
    my_list = final.values.tolist()

    # create dictionary to group the values by their first element
    grouped = {}
    for item in my_list:
       if item[0] in grouped:
          grouped[item[0]].append(item[1])
       else:
          grouped[item[0]] = [item[1]]

    # convert the dictionary to the desired list format
    result = [[k, v] for k, v in grouped.items()]

    # sort the result list by the first element of each sublist
    result.sort(key=lambda x: x[0])

    # convert the first element of each sublist to a list
    for sublist in result:
        sublist[0] = [sublist[0]]

    # combine sublists with the same second element
    final_result = []
    for sublist in result:
        found = False
        for existing_sublist in final_result:
            if sublist[1] == existing_sublist[1]:
                existing_sublist[0].extend(sublist[0])
                found = True
                break
        if not found:
            final_result.append(sublist)

    return final_result