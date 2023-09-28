students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])


my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)

# TODO исправить код


def find_all_interests_and_surnames_length(data):
    all_interest = []
    surname_length = []
    for i_id, i_info in data.items():
        for i_key, i_value in i_info.items():
            if i_key == 'interests':
                all_interest += i_value
            elif i_key == 'surname':
                surname_length += i_value
    return all_interest, len(surname_length)


all_interests, surnames_length = find_all_interests_and_surnames_length(students)

pairs = []
for ids, value in students.items():
    for info, age in value.items():
        if info == 'age':
            pair = (ids, age)
            pairs.append(tuple(pair))

print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', all_interests)
print('Общая длина всех фамилий студентов:', surnames_length)

