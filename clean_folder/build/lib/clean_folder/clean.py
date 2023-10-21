import sys
import re
import shutil
from pathlib import Path

# Списки файлів
# Зображення ('JPEG', 'PNG', 'JPG', 'SVG')
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
# Відео('AVI', 'MP4', 'MOV', 'MKV')
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
# Документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
DOC_DOCUM = []
DOCX_DOCUM = []
TXT_DOCUM = []
PDF_DOCUM = []
XLSX_DOCUM = []
PPTX_DOCUM = []
# Музика ('MP3', 'OGG', 'WAV', 'AMR')
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
# Архіви ('ZIP', 'GZ', 'TAR')
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
MY_OTHER = []

# Теки файлів
FOLDERS = []
EXTENSIONS = set()
UNKNOWN_EXTENSIONS = set()

NAME_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,

    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MRV': MKV_VIDEO,

    'DOC': DOC_DOCUM,
    'DOCX': DOCX_DOCUM,
    'TXT': TXT_DOCUM,
    'PDF': PDF_DOCUM,
    'XLSX': XLSX_DOCUM,
    'PPTX': PPTX_DOCUM,

    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,

    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES, 
    'TAR': TAR_ARCHIVES,
}



def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи об`єкт папка
            if item.name not in ('images', 'video', 'documents', 'audio', 'archives', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  # Беремо розширення файлу
        print(extension)
        full_name = folder / item.name  # Беремо повний шлях до файлу
        # print(full_name)
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = NAME_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN_EXTENSIONS.add(extension) # Невідомі розширення
                MY_OTHER.append(full_name)




CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_name = re.sub(r'[^\w.]', '_', name.translate(TRANS))
    return translate_name




def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))



def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    scan(folder)
    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    for file in OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in DOC_DOCUM:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in DOCX_DOCUM:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in TXT_DOCUM:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in PDF_DOCUM:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in XLSX_DOCUM:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in PPTX_DOCUM:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives')
    for file in GZ_ARCHIVES:
        handle_archive(file, folder / 'archives')
    for file in TAR_ARCHIVES:
        handle_archive(file, folder / 'archives')
    for file in MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')
    for folder in FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')


def start():
    if sys.argv[1]:
        folder_process = Path(sys.argv[1])
        main(folder_process)
