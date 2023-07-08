# AUTOGENERATED! DO NOT EDIT! File to edit: ../_nbdev.ipynb.

# %% auto 0
__all__ = ['exception', 'answer']

# %% ../_nbdev.ipynb 6
from IPython.core.magic import register_line_magic, register_cell_magic, needs_local_scope
from IPython import get_ipython
import re, sys

# %% ../_nbdev.ipynb 9
@register_cell_magic('exception')
def exception(line, cell):
    ip = get_ipython()
    try:
        exec(cell, None, ip.user_ns)
    except Exception as e:
        etype, value, tb = sys.exc_info()
        value.__cause__ = None  # suppress chained exceptions
        ip._showtraceback(etype, value, ip.InteractiveTB.get_exception_only(etype, value))

# %% ../_nbdev.ipynb 22
@register_line_magic('answer')
def answer(inputs):
    '''
    This is a cell magic called answer that allows tutorial goers to import the correct answer from the key. 
    '''
    words = []
    for word in inputs.split(' '):
        if not word.startswith('#'):
            words.append(word)
        else:
            break
    
    assert len(words) == 2,  "%answer takes a filepath and a cell number"
    filepath = words[0]
    cell_number = int(words[1])
    
    with open(filepath, 'r') as file:
        lines = file.readlines()

    pattern = r'# %% .+ \d+'
    start_line = None
    end_line = None

    for i, line in enumerate(lines):
        if re.match(pattern, line):
            match = re.search(r'\d+', line)
            if match and int(match.group()) == cell_number:
                start_line = i + 1
                break
    if start_line is not None:
        for i in range(start_line, len(lines)):
            if re.match(pattern, lines[i]):
                end_line = i
                break
        else:
            end_line = len(lines)
            
    if start_line is not None and end_line is not None:
        code_chunk = f"# %answer {inputs}\n" + ''.join(lines[start_line:end_line])
        code_chunk = code_chunk.rstrip("\n")
        get_ipython().set_next_input(code_chunk, replace=True)
    else:
        print(f"Cell number {cell_number} not found in the Python file.")
