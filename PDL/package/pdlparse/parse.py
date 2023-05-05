# TODO: Add skips for variables with `priv` in the same line in all get functions
# TODO: Add a function to retrive variables from file and create program vars (https://stackoverflow.com/questions/924700/best-way-to-retrieve-variable-values-from-a-text-file)

import os, sys

'''
__KEYWORDS__
class - a place to store variables and data
priv - declares a variable as exclusive to .pdl file
new - creates a copy of variable similar to handle
__TYPES__
str - declares a variable as a string
int - declares a variable as integer
lst - uses brackets and commas to create list's
flt - a floating point number
raw - used to declare all back-slashes to be ignored
bol - true, false, null
__COMMENTS__
// - line comment
/* - start block
*/ - end block
'''


class utility:
  def typeProcessor(assumed_type):
    if 'str' in assumed_type:
      return 'string'
    elif 'int' in assumed_type:
      return 'integer'
    elif 'lst' in assumed_type:
      return 'array'
    elif 'bol' in assumed_type:
      return 'boolean'
    elif 'raw' in assumed_type:
      return 'raw_string'
    elif 'flt' in assumed_type:
      return 'floating_point'
    else:
      raise Exception('ENGINE-[ERROR] A fatal function was passed a incomprehensible argument')

  def findClass(library, var, type, value):
    # Searches for variables class and returns it
    if not os.path.exists(library):
      raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

    with open(library, 'r+') as file:
      file_content = file.read()
      if var in file_content:
        for line in file_content.split('\n'):
          if '{' in line:
            class_index = file_content.splitlines().index(line)
            index = line.find('{')
            indextr = line.find('class')
          if var and type and value in line:
            line_index = file_content.splitlines().index(line)
            if line_index > class_index:
              line_diffrence = line_index - class_index
            else:
              line_diffrence = class_index - line_index
            target_line = file_content.splitlines()[line_index - line_diffrence]
            class_name = target_line[indextr:index - 1]

      return class_name.replace('class ', '')


def scrap_library(library):
  # Get all variables in library
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r+') as file:
    retlist = []
    file_content = file.read()
    for line in file_content.split('\n'):
      for fline in file_content.split('\n'):
        if '=' in fline:
          index = fline.find('=')
          if fline[index + 2:].isdigit() or "'" not in fline[index + 2:]:
            indexer = fline[index + 2:]
          else:
            indexer = fline[index + 3:]
          found = fline.find('=')
          value = indexer.replace("'", '')
          type = utility.typeProcessor(fline[0:5])
          raw_type = fline[0:5]
          var = fline[5:found - 1].replace(' ', '')
          class_name = utility.findClass(library, var, raw_type, value)
          retlist.append(f'{class_name}.{var} = {value}, {type}')
      return retlist


def get_variable(library, variable):
  # Get a variables value based on its name
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r') as Fin:
    content = Fin.read()
  if variable in content:
    with open(library, 'r+') as file:
      file_content = file.read()
      for line in file_content.split('\n'):
        if variable in line:
          if '=' in line:
            index = line.find('=')
            value = line[index + 3:].replace("'", '')
            type = utility.typeProcessor(line[0:5])
          return str(f'{value}, {type}')
  else:
    raise Exception(f'[ERROR] Package pdlparse cannot find {variable} in {library}.')


def filter_file(library, word):
  # Remove given word from library
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')
  with open(library, "r+") as Fin:
    content = Fin.read()
  if word in content:
    with open(library, "w+") as Fout:
      write_item = content.replace(word, "")
      Fout.write(write_item)
  else:
    raise Exception(f'[ERROR] {word} cannot be found in {library}')


def get_strings(library):
  # Get all strings from library
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r+') as file:
    retlist = []
    file_content = file.read()
  for line in file_content.split('\n'):
    if "'" and "str" in line:
      index = line.find("'")
      string = line[index:].replace("'", "")
      retlist.append(string)
  return retlist


def get_class(library, target_class):
  # Get all variables in given class
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r') as Fin:
    content = Fin.read()
  if target_class in content:
    with open(library, 'r+') as file:
      file_content = file.read()
      for line in file_content.split('\n'):
        if target_class in line:
          if '{' in line:
            retlist = []
            for fline in file_content.split('\n'):
              if '=' in fline:
                index = fline.find('=')
                if fline[index + 2:].isdigit() or "'" not in fline[index + 2:]:
                  indexer = fline[index + 2:]
                else:
                  indexer = fline[index + 3:]
                found = fline.find('=')
                value = indexer.replace("'", '')
                type = utility.typeProcessor(fline[0:5])
                var = fline[5:found - 1].replace(' ', '')
                retlist.append(f'{var} = {value}, {type}')
              if '};' in fline:
                file.close()
          return retlist
  else:
    raise Exception(f'[ERROR] Package pdlparse cannot find {target_class} in {library}.')


def get_type(library, target_type):
  # Get all variables with given type
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r') as Fin:
    content = Fin.read()
  if target_type in content:
    with open(library, 'r+') as file:
      file_content = file.read()
      for line in file_content.split('\n'):
        if target_type in line:
          retlist = []
          for fline in file_content.split('\n'):
            if '=' in fline:
              index = fline.find('=')
              if fline[index + 2:].isdigit() or "'" not in fline[index + 2:]:
                indexer = fline[index + 2:]
              else:
                indexer = fline[index + 3:]
              found = fline.find('=')
              value = indexer.replace("'", '')
              var = fline[5:found - 1].replace(' ', '')
              if fline[0:5].replace(' ', '') == target_type:
                retlist.append(f'{var} = {value}')
              else:
                pass
          return retlist
  else:
    raise Exception(f'[ERROR] Package pdlparse cannot find {target_type} in {library}.')


def get_value(library, target_value):
  # Get information about a variable based on its value
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r') as Fin:
    content = Fin.read()
  if target_value in content:
    with open(library, 'r+') as file:
      file_content = file.read()
      for line in file_content.split('\n'):
        if target_value in line:
          retlist = []
          for fline in file_content.split('\n'):
            if '=' in fline:
              index = fline.find('=')
              if fline[index + 2:].isdigit() or "'" not in fline[index + 2:]:
                indexer = fline[index + 2:]
              else:
                indexer = fline[index + 3:]
              found = fline.find('=')
              value = indexer.replace("'", '')
              var = fline[5:found - 1].replace(' ', '')
              type = fline[0:5]
              class_name = utility.findClass(library, var, type, value)
              if value == target_value:
                retlist.append(f'{class_name}.{var} = {value}')
              else:
                pass
          return retlist
  else:
    raise Exception(f'[ERROR] Package pdlparse cannot find {target_value} in {library}.')


def get_comments(library):
  # Gets all comments from given library
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find file {library}.')

  with open(library, 'r+') as file:
    retlist = []
    file_content = file.read()
  for line in file_content.split('\n'):
    if "//" in line:
      index = line.find("//")
      string = line[index:].replace("// ", "")
      retlist.append(string)
  return retlist

