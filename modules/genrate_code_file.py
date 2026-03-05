import uuid
from pathlib import Path



language_extentsion = {
    0:'c',
    1:'cpp',
    2:'java',
    3:'js',
    4:'rs',
    5:'py'
}


def genrate_code_file(language:int,code:str):
    id = uuid.uuid4()
    filename =  str(id) + "." + language_extentsion[language]
    folder_path = Path("temp")
    file_path = folder_path / filename
    folder_path.mkdir(parents=True,exist_ok=True)
    with open(file_path,"w") as f:
        f.writelines(code)
    return file_path,id
    