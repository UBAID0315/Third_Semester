word_list = ["Apple", "Banana", "Avocado", "Cherry", "Apricot", "Graphes"]

filtered = list(filter(lambda string: string[0]=='A',word_list))

print(f'Words start with A: {filtered}')
print(f'Total count: {len(filtered)}'
