"""
A ideia é: Fazer com que, script.py inserte um print("Hello World") no desired_script.py e após isso, execute o desired_script.py
"""

import tempfile, importlib.util, os, shutil

try:
  os.mkdir("temp")
except FileExistsError:
  pass

tempfile = tempfile.NamedTemporaryFile(mode='w+', suffix=".py", dir="./temp", delete=False)
tempfile.write('print("Hello World")\n')
tempfile.close()

temp_name = tempfile.name[tempfile.name.rfind("\\") + 1:]

module_spec = importlib.util.spec_from_file_location(temp_name, tempfile.name)
module_import = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module_import)

input()

shutil.rmtree("temp")
