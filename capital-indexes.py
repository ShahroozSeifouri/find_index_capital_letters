def capital_indexes(user_str):
    capital_index=[]
    for index,letters in enumerate(user_str):
        if letters.isupper():
            capital_index.append(index)

    return capital_index
print(capital_indexes('ShaHroOz'))


