from pprint import pprint

documents = [
  {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
  {'type': 'insurance', 'number': '10009'}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит

def get_holder_name(documents_list):
  number_user_input = input('Введите номер документа: ')
  for document in documents_list:
    if number_user_input == document['number']:
      print('Имя владельца: ', document['name'])
      break
  print('Документ не найден')


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"

def print_documents_list(documents_list):
  for document in documents_list:
    print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


# ln – list name – команда, которая выведет инмена всех владельцев",
# если удалить строку (assert 'name' in....) тоже все будет работать и ловиться будет именно KeyError

def print_documents_list_name(documents_list):
  for document in documents_list:
      try:
          assert 'name' in document.keys(), f'У документа "{document["number"]}" нет ключа "name"'
          print(f'"{document["name"]}"')
      except Exception as e:
          print(f'{type(e)}: {e}')


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def get_shelf_number(documents_list, shelfs):
  number_user_input = input('Введите номер документа: ')
  for number in shelfs.keys():
    count = 0
    for document in shelfs[number]:
      if number_user_input == document:
        count = 1
        print('Номер полки: ', number)
        break
    if count == 1:
      break
  print('Документ не найден')

# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться

def add_new_document(documents_list, shelfs):
  number_user_input = input('Введите номер нового документа: ')
  type_user_input = input('Введите тип документа: ')
  name_user_input = input('Введите имя владельца: ')
  shelf_user_input = input('Введите номер полки: ')
  new_document = {'type': type_user_input, 'number': number_user_input, 'name': name_user_input}
  documents_list.append(new_document)
  if shelf_user_input not in shelfs.keys():
    shelfs[shelf_user_input] = []
  shelfs[shelf_user_input].append(number_user_input)
# для проверки
  pprint(documents_list)
  pprint(shelfs)

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок

def delete_document(documents_list, shelfs):
  number_user_input = input('Введите номер документа: ')
  for document in documents_list:
    if number_user_input == document['number']:
      documents_list.remove(document)
      for number in shelfs.keys():
        for document in shelfs[number]:
          if number_user_input == document:
            shelfs[number].remove(document)
      break
  print('Документ не найден')
# для проверки
  pprint(documents_list)
  pprint(shelfs)

# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую

def move_document(documents_list, shelfs):
  number_user_input = input('Введите номер документа: ')
  for number in shelfs.keys():
    # count = 0
    for document in shelfs[number]:
      if number_user_input == document:
        # count = 1
        shelfs[number].remove(document)
        shelf_user_input = input('Введите номер новой полки: ')
        if shelf_user_input not in shelfs.keys():
          shelfs[shelf_user_input] = []
        shelfs[shelf_user_input].append(number_user_input)
        return
    # if count == 1:
    #   break
  print('Документ не найден')
# для проверки
  pprint(documents_list)
  pprint(shelfs)

# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень

def add_shelf(shelfs):
  shelf_user_input = input('Введите номер новой полки: ')
  if shelf_user_input not in shelfs.keys():
    shelfs[shelf_user_input] = []
  else: print(f'Полка "{shelf_user_input}" уже существует')
# для проверки
  pprint(shelfs)

def main():
  while True:
    user_input = input('Введите команду (p,l,ln,s,a,d,m,as,q): ')
    if user_input == 'p':
      get_holder_name(documents)
    elif user_input == 'l':
      print_documents_list(documents)
    elif user_input == 'ln':
      print_documents_list_name(documents)
    elif user_input == 's':
      get_shelf_number(documents_list=documents, shelfs=directories)
    elif user_input == 'a':
      add_new_document(documents_list=documents, shelfs=directories)
    elif user_input == 'd':
      delete_document(documents_list=documents, shelfs=directories)
    elif user_input == 'm':
      move_document(documents_list=documents, shelfs=directories)
    elif user_input == 'as':
      add_shelf(directories)
    elif user_input == 'q':
      print('До свидания')
      break
    else: print('Неверная команда')

main()