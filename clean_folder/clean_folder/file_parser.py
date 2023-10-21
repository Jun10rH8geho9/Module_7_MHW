import re
import sys
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

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     folder_process = Path(sys.argv[1])
    #     scan(Path(folder_process))
    # else:
    #     print("Please provide a folder")
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')

    print(f'VIDEO avi: {AVI_VIDEO}')
    print(f'VIDEO mp4: {MP4_VIDEO}')
    print(f'VIDEO mov: {MOV_VIDEO}')
    print(f'VIDEO mkv: {MKV_VIDEO}')

    print(f'Documents doc: {DOC_DOCUM}')
    print(f'Documents docx: {DOCX_DOCUM}')
    print(f'Documents txt: {TXT_DOCUM}')
    print(f'Documents pdf: {PDF_DOCUM}')
    print(f'Documents xlsx: {XLSX_DOCUM}')
    print(f'Documents pptx: {PPTX_DOCUM}')

    print(f'AUDIO mp3: {MP3_AUDIO}')
    print(f'AUDIO ogg: {OGG_AUDIO}')
    print(f'AUDIO wav: {WAV_AUDIO}')
    print(f'AUDIO amr: {AMR_AUDIO}')

    print(f'Archives zip: {ZIP_ARCHIVES}')
    print(f'Archives gz: {GZ_ARCHIVES}')
    print(f'Archives tar: {TAR_ARCHIVES}')
    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN_EXTENSIONS: {UNKNOWN_EXTENSIONS}')

