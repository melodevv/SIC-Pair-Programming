fruits_dic = {
    'apple': 6000,
    'melon': 3000,
    'banana': 5000,
    'orange': 4000}
dict_keys = list(fruits_dic.keys())
print('dict_keys(', dict_keys, ')')
if 'apple' in fruits_dic:
    print('apple is in fruits_dic')
else:
    print('apple is not in fruits_dic')

if 'mango' in fruits_dic:
    print('mango is in fruits_dic')
else:
    print('mango is not in fruits_dic')
