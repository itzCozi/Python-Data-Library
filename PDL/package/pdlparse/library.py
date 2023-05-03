import os, sys


def get_libs(dir):
  # Gets all .pdl files in dir
  retlist = []
  for r, d, f in os.walk(dir):
    for file in f:
      if '.pdl' in file:
        itemobj = os.path.relpath(f'{r}/{file}')
        retlist.append(itemobj)
  
  return retlist


def get_lib_info(library):
  # Returns information on the given library
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {library}.')
  
  with open(library, 'r') as file:
    file_content = file.read()
  if '=' or '{' in file_content:
    var_count = 0
    class_count = 0
    for line in file_content.splitlines():
      if '=' in line:
        var_count += 1
      if '{' in line:
        class_count += 1
      else:
        pass
  
  else:
    raise Exception(f'ERROR: Package pdlparse cannot find vars or classes in {library}.')
  return f'variable# = {var_count} class# = {class_count}'


def get_main_lib(base_dir):
  # Finds main library if there are any
  if not os.path.exists(base_dir):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {base_dir}.')
  
  retlist = []
  for r, d, f in os.walk(base_dir):
    for file in f:
      if 'main' in file:
        if '.pdl' in file:
          itemobj = os.path.relpath(f'{r}/{file}')
          retlist.append(itemobj)
        else:
          pass
  
  if len(retlist) == 0:
    retlist.append('No main library found.')
  return retlist


def read_lib(library, aloud=False):
  # Reads the given library aloud or returns it
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {library}.')
  
  with open(library, 'r') as file:
    retlist = []
    file_content = file.read()
    
  for line in file_content.splitlines():
    if aloud != False:
      retlist.append(line)
    else:
      print(line)
  if aloud != False:
    return retlist


def format_lib(library):
  # Fixes any soft-errors found in library
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {library}.')
  
  with open(library, 'r') as file:
    file_content = file.read()
  for line in file_content.splitlines():
    if '}' in line:
      index = line.find('}')
      if not ';' in line:
        with open(library, 'w') as edit:
          replacement = file_content.replace('}', '};')
          edit.write(replacement)
          continue
    if '{' in line:
      index = line.find('{')
      name = line[0:index-1]
      if not 'class' in line:
        with open(library, 'w') as edit:
          replacement = file_content.replace(f'{name}', f'class {name}')
          edit.write(replacement)
          continue
    if 'int' in line:
      if "'" in line:
        index_var = line.find("'")
        variable = line[index_var+1:-1]
        with open(library, 'w') as edit:
          replacement = file_content.replace(f"'{variable}'", f"{variable}")
          edit.write(replacement)
          continue
    if 'str' in line:
      if not "'" in line:
        index_var = line.find('=')
        variable = line[index_var+2:]
        with open(library, 'w') as edit:
          replacement = file_content.replace(f"{variable}", f"'{variable}'")
          edit.write(replacement)
          continue
    if 'flt' in line:
      if "'" in line:
        index_var = line.find("'")
        variable = line[index_var+1:-1]
        with open(library, 'w') as edit:
          replacement = file_content.replace(f"'{variable}'", f"{variable}")
          edit.write(replacement)
          continue
    if 'raw' in line:
      if not "'" or '/' in line:
        index_var = line.find('=')
        variable = line[index_var+2:]
        with open(library, 'w') as edit:
          replacement = file_content.replace(f"{variable}", f"/'{variable}'/")
          edit.write(replacement)
          continue
    else:
      pass


def rm_library(library):
  # Burry the library 6-feet under. (delete it)
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {library}.')
  
  try:
    os.remove(library)
  except Exception as e:
    raise Exception(f'ERROR: An unknown error occurred during runtime \n{e}\n')


def remove_comments(library):
  # Removes all comments from a library
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find file {library}.')

  with open(library, 'r+') as file:
    retlist = []
    file_content = file.read()
  for line in file_content.split('\n'):
    if "//" in line:
      index = line.find("//")
      string = line[index:].replace("// ", "")
      retlist.append(string)
    for item in retlist:
      with open(library, 'w') as edit:
        replacement = file_content.replace(string, '')
        edit.write(replacement)
  return retlist

