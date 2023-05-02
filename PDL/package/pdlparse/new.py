import os, sys


def create_lib(path, name):
  if not os.path.exists(path):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find {path}.')
  
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
  if not os.path.exists(library):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find {library}')
  file_path = os.path.dirname(library)
  if not '.' in script_name:
    new_file = f'{file_path}/{script_name}.py'
  else:
    raise Exception(f'ERROR: Package pdlparse found `.` in {script_name} variable')
  
  with open(new_file, 'w') as new:
    new.write("import os, sys \n")
    new.write("import pdlparse as pdl \n")
    new.write("variables = pdl.parse.scrap_library('test.pdl')")


def create_manifest(dir):
  if not os.path.exists(dir):
    raise FileNotFoundError(f'ERROR: Package pdlparse cannot find {dir}')
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

