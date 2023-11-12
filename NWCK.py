def distance_tree(tree, x, y):
    x_index = tree.find(x)
    y_index = tree.find(y)
    t = [char for char in tree[min(x_index, y_index):max(x_index, y_index)] if char in [')', '(', ',']]
    bracket = ''.join(t)

    while '(,)' in bracket:
        bracket = bracket.replace('(,)', '')

    if bracket.count('(') == len(bracket) or bracket.count(')') == len(bracket):
        return len(bracket)
    elif bracket.count(',') == len(bracket):
        return 2
    else:
        return bracket.count(')') + bracket.count('(') + 2

def read_goofy_format(input_mess):
    for entry in input_mess:
        input_list = [line.strip().replace(';', '') for line in entry.split('\n') if len(line.strip()) > 0]
        for i in range(0, len(input_list), 2):
            tree = input_list[i]
            x, y = input_list[i + 1].split(' ')
            print(distance_tree(tree, x, y), end=" ")
        print()

input_mess = ["""#paste input here"""]
read_goofy_format(input_mess)