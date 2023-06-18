
def input_new():
    name = input("new name: ")
    data = input("new data birth: ")
    str_new = f"{name} | {data} \n"
    return str_new

def prepare_for_Edit_Delete(serch_data:str):
    result = dict()
    find_name = serch_data
    with open('data.csv', "r") as file:
        user_full = file.read().splitlines()
    for i in range(len(user_full)):
        result[i] = user_full[i]
    # print(result)
    for key, value in result.items():
        if find_name in value:
            print(f"{key} {result[key]}")
    serch_data
    return result

class Phone_Dict():

    def cread_data(self):
        name = input("new name: ")
        data_birth = input("data birth: ")
        str1 = f"{name} | {data_birth} \n"
        with open("data.txt", "a") as file:
            file.writelines(str1)

    def read_data(self):
        with open('data.csv', "r") as file:
            print(file.read())

    def edit_data(self, serch_data: str):
        result = prepare_for_Edit_Delete(serch_data)
        print("input number person which you want change: ")
        person = int(input())
        for key, value in result.items():
            if person == key:
                print("input new person, last will be change... ")
                user_updat = input_new()
                result[key] = user_updat
        with open('data.txt', "w") as file:  # здесь используем атрибут перезаписи файла, поэтому без отдельной функции
            dict_copy = dict()
            for key, val in result.items():
                if val != '':
                    dict_copy[key] = val
                    str11 = f"{dict_copy[key]} \n"
                    file.writelines(str11)
        return result

    def delete_Data(self, serch_data: str):
        result = prepare_for_Edit_Delete(serch_data)
        print("input number person which you want delete: ")
        person = int(input())
        for key, value in list(
                result.items()):  # RuntimeError: dictionary changed size during iteration, if not using List()
            if person == key:
                del result[person]
            # if value == '':
            #     del result[person]
        # print(result)
        with open('data.csv', "w") as file:  # здесь используем атрибут перезаписи файла, поэтому без отдельной функции
            for key, val in result.items():
                str11 = f"{val}\n"
                file.writelines(str11)
        return result