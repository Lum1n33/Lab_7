def find_max_substring_multiplicity(word, str):
    multiplicity = 0
    max_multiplicity = 0
    start_index = 0

    while start_index <=len(word) - len(str):
        if word[start_index:start_index + len(str)] == str:
            multiplicity += 1
            max_multiplicity = max(max_multiplicity, multiplicity)
            start_index += len(str)
        else:
            multiplicity = 0
            start_index += 1
    
    return max_multiplicity


word = input("Введите запрос:")
str = input("Введите подстроку:")

max_multiplicity = find_max_substring_multiplicity(word, str)
print(f"Кратность подстроки '{str}' в запросе '{word}': {max_multiplicity}")
