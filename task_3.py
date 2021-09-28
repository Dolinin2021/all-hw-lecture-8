import os

PATH = './task_3'


def get_list_files(path_name):

    hope_dict = {}
    res_list = []

    with os.scandir(path_name) as list_files:
        for entry in list_files:
            if entry.is_file():
                    with open(path_name+'/'+entry.name, encoding='windows-1251') as file_obj:
                        tmp_file = file_obj.readlines()
                        hope_dict[entry.name] = (len(tmp_file), tmp_file)
                        res_list.append((entry.name, hope_dict[entry.name]))
        res_list.sort(key=lambda temp: temp[1][0])

    with open ('res.txt','w') as document:
        for variable in res_list:
            document.write(variable[0])
            document.write('\n')
            document.write(str(variable[1][0]))
            document.write('\n')
            variable_temp = variable[1][1]
            document.writelines(variable_temp)
            document.write('\n')


get_list_files(PATH)