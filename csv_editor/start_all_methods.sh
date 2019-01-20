#!/bin/sh
set -eu
set -o pipefail

METHOD1="full copy"
METHOD2="workbook copy"

# Запуск в режиме полного копирования
ansible-playbook play.yml -i inventory/inventory -e "method_name='${METHOD1}'"
# Запуск в режиме копирования на уровне рабочей книги
ansible-playbook play.yml -i inventory/inventory -e "method_name='${METHOD2}'"