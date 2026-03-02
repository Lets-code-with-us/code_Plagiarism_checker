import re
from modules.genrate_code_file import genrate_code_file

language_id = {
    0: 'c',
    1: 'cpp',
    2: 'java',
    3: 'node',
    4: 'rust',
    5: 'python'
}


def remove_c_style_comments(code: str) -> str:
    # Remove single-line comments
    code = re.sub(r'//.*', '', code)

    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

    return code

def remove_python_comments(code: str) -> str:
    # Remove # comments
    code = re.sub(r'#.*', '', code)

    # Remove triple-quoted strings (""" or ''')
    code = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', code)

    return code


def preprocess_code(language: int, code: str):
    lang = language_id[language]
    corpus = []
    temp = []

    match lang:
        case "c" | "cpp" | "java" | "node":
            code = remove_c_style_comments(code)

        case "rust":
            code = remove_c_style_comments(code)
            # Remove Rust doc comments
            code = re.sub(r'///.*', '', code)
            code = re.sub(r'//!.*', '', code)

        case "python":
            code = remove_python_comments(code)

        case _:
            raise ValueError("Unsupported language")
    file_path = genrate_code_file(language, code.strip())
    with open(file_path,'r') as f:
        fs = f.read()
        temp = fs.split(" ")
    for i in temp:
        if i != '' and i != '\n':
            corpus.append(i)    
    return corpus