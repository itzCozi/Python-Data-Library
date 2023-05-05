import os, sys
import string
import random


def create_lib(path, name):
  # Creates new library
  if not os.path.exists(path):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find {path}.')

  new_file = f'{path}/{name}.pdl'
  with open(new_file, 'w') as file:
    file.write('''/*
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
*/
    \n''')
    file.write('class main { \
      \n  int number = 23 \
      \n};')


def create_lib_script(library, script_name):
  # Automaticly creates a library script
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find {library}')
  file_path = os.path.dirname(library)
  if not '.' in script_name:
    new_file = f'{file_path}/{script_name}.py'
  else:
    raise Exception(f'[ERROR] Package pdlparse found `.` in {script_name} variable')

  with open(new_file, 'w') as new:
    new.write("import os, sys \n")
    new.write("import pdlparse as pdl \n\n")
    new.write(f"variables = pdl.parse.scrap_library('{library}')")


def create_manifest(dir):
  # Create a new manifest with all files in folder
  if not os.path.exists(dir):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find {dir}')
  new_file = f'{dir}/MANIFEST'

  with open(new_file, 'a') as file:
    libs = []
    file.write('-_FILES_-\n')
    for r, d, f in os.walk(dir):
      for item in f:
        if 'MANIFEST' in item:
          f.remove(item)
        if '.pdl' in item:
          libs.append(item)
        else:
          file.write(f'{item}\n')
    file.write('-_LIBS_-\n')
    for item in libs:
      file.write(f'{item}\n')


def create_class(library, class_name):
  # Create a new class in given library
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find {library}')
  start_bracket = '{'
  end_bracket = '}'

  try:
    with open(library, 'a+') as file:
      file.write(f"""
class {class_name} {start_bracket}
  str placeholder = 'Replace me'
{end_bracket};
""")
      file.close()
  except Exception as e:
    raise Exception(f'[ERROR] An unknown runtime error occurred. \n{e}\n')


def create_lib_id(library):
  if not os.path.exists(library):
    raise FileNotFoundError(f'[ERROR] Package pdlparse cannot find {library}')
  if os.path.getsize(library) == 0:
    raise Exception(f'[ERROR] Given library {library} is too small.')
  alphabet = string.ascii_letters + string.digits
  lenght_list = [6, 8, 16]
  id = []

  for i in range(random.choice(lenght_list)):
    id.append(random.choice(alphabet))

  with open(library, 'r') as file:
    content = file.read()
    lines = content.splitlines()
    first_line = lines[0]
    content = content.replace(first_line, f"{''.join(id)}")
  with open(library, 'w') as edit:
    edit.write(content)
