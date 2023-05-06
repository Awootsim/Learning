
# path = r'D:\Data\MyFiles\file.png'
#  print(path[path.rfind("\\") + 1:path.rfind(".")])  # Печать названия файла
#  print(path[:path.find("\\")])  # Печать диска
#  folder = path[path.find("\\")+1:]  # Сократил путь файла до названия корневой папки
#  print(folder[:folder.find("\\")])  # Печать корневой папки

text = r'D:\Data\MyFiles\file.png'
print(text[text.rfind("\\") + 1: text.rfind(".")])  # Файл
print(text[:text.find('\\')])  # Диск
print(text[text.find('\\') + 1:text.find('\\', text.find('\\') + 1)])  # Папка

