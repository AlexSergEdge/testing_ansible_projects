#coding=utf-8
import pytest #ansible-pytest
import os

# Command to call module:
# pytest -p no:cacheprovider library/test_pytest_ansible.py --ansible-inventory inventory/inventory --ansible-host-pattern all
# Command to add module to ANSIBLE_LIBRARY
# export ANSIBLE_LIBRARY=./path/to/custom/modules_dir/
# в данном случае export ANSIBLE_LIBRARY=./

# полезные ссылки
# https://pypi.org/project/pytest-ansible/
# https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#information-discovered-from-systems-facts

# Используем fixture с названием "ansible_module"
def test_ansible_module(ansible_module):
    # Input data
    output_file_path1 = '/syncfolder/excel_files/new_ansible_test_output_excel_uri.xlsx'
    output_file_path2 = '/syncfolder/excel_files/new_ansible_test_output_excel_uri2.xlsx'
    input_file_path ='/syncfolder/excel_files/input_excel_uri.xlsx'
    input_data = [
        ['D1','E0','D2','E1',],
        ['D1','E0','D2','E1',],
        ['D1','E0','D2','E1',],
        ['D1','E0','D2','E1',],
        ['D1','E0','D2','E1',],
    ]
    input_header = ['Name A', 'Interface A', 'Name B', 'Interface B',]
    # Method 1 test
    output = ansible_module.create_csv(
        header_data=input_header,
        function_name="full copy",
        table_data=input_data,
        input_excel=input_file_path,
        output_excel1=output_file_path1,
        output_excel2=output_file_path2,
    )
    # Проверяем результат
    # Если файл еще не был создан
    if not os.path.isfile(output_file_path1):
        for (host, result) in output.items():
            print(result)
            assert 'Successfully copied excel data' in result['msg']
    # Если файл уже был создан
    else:
        for (host, result) in output.items():
            print(result)
            assert 'File already exists and correct. Do nothing' in result['message']
    # Testing method 2
    output = ansible_module.create_csv(
        header_data=input_header,
        function_name="workbook copy",
        table_data=input_data,
        input_excel=input_file_path,
        output_excel1=output_file_path1,
        output_excel2=output_file_path2,
    )
    # Проверяем результат
    for (host, result) in output.items():
        print(result)
        assert 'Successfully created new file' in result['meta']