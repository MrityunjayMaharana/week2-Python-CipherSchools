my_list = ['good', 'for']
my_list.append('goodthing')
print (my_list)

a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)


input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {}
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3
print("Output Dictionary using for loop:",output_dict )


state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dict_using_comp = {key:value for (key, value) in zip(state, capital)}
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)