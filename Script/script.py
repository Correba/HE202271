"""Module pour utiliser des options en ligne de commande"""
import argparse
import shutil
import os

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv",
         ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc",
         ".wav", ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif")


def is_audio(file: str) -> bool:
    """
    PRE : file est un fichier a vérifier
    POST : Renvoie si le fichier est un audio
    """
    return os.path.splitext(file)[1] in audio


def is_video(file: str) -> bool:
    """
    PRE : file est un fichier a vérifier
    POST : Renvoie si le fichier est une vidéo
    """
    return os.path.splitext(file)[1] in video


def is_image(file: str) -> bool:
    """
    PRE : file est un fichier a vérifier
    POST : Renvoie si le fichier est une image
    """
    return os.path.splitext(file)[1] in img


def find_ext(file: str) -> str or int:
    """
    PRE : file est un fichier où on cherche l'extension
    POST : - Renvoie l'extension du fichier
           - Si le fichier n'a pas d'extension renvoie -1
    """
    index = file.find('.')
    if index != -1:
        return file[index + 1::]

    return index


def find_directory(file: str, out: str) -> str:
    """
    PRE : - file est un fichier qu'on cherche dans quel sous-dossier rangé
          - out est l'adresse du dossier parent
    POST : Renvoie l'adresse du dossier ou rangé file
    """
    if args.audio and is_audio(file):
        return out + 'audio'

    if args.video and is_video(file):
        return out + 'video'

    if args.image and is_image(file):
        return out + 'image'

    if find_ext(file) != -1:
        return out + find_ext(file)

    return out


def directory_exist(directory: str) -> None:
    """
    PRE : directory est le dossier qu'on cherche à vérifier si il existe
    POST : crée le dossier directory si il n'existe pas
    """
    if not os.path.exists(directory):
        os.mkdir(directory)


def fill_lists(directory: str) -> None:
    """
    PRE : directory est le dossier où on va sortir le contenu a organisé
    POST : Rempli les listes files et directories avec des fichiers et/ou dossiers se trouvant dans directory
    """
    for file in os.listdir(directory):
        file_path = directory + file
        if os.path.isfile(file_path):
            files.append(file_path)
        else:
            directories.append(file_path + '/')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organise les fichiers d\'un dossier selon leur extension')
    parser.add_argument('--input', type=str, default='.', metavar=' dossier :',
                        help='le dossier à ranger', required=True)
    parser.add_argument('--output', type=str, default='.', metavar='dossier :',
                        help='le dossier ou tout sera ranger')
    parser.add_argument('--audio', action='store_true',
                        help='Crée un dossier pour tous les fichiers audio')
    parser.add_argument('--video', action='store_true',
                        help='Crée un dossier pour tous les fichiers vidéos')
    parser.add_argument('--image', action='store_true',
                        help='Crée un dossier pour tous les fichiers d\'image')
    parser.add_argument('--recursive', action='store_true',
                        help='Inclure le contenu des (sous-)dossiers du dossier input dans le tri')
    args = parser.parse_args()

    files = []  # Une liste des fichiers dans le dossier input
    directories = []  # Une liste des dossiers dans le dossier input

    if args.input[-1] == '/':
        path_in = args.input
    else:
        path_in = args.input + '/'

    if args.output:
        directory_exist(args.output)

        if args.output[-1] == '/':
            path_out = args.output
        else:
            path_out = args.output + '/'
    else:
        path_out = path_in

    fill_lists(path_in)

    if args.recursive:
        while len(directories) > 0:
            directory = directories.pop()
            fill_lists(directory)

    for file in files:
        directory = find_directory(file, path_out)
        directory_exist(directory)

        if find_ext(file) != -1:
            shutil.move(file, directory)
        else:
            shutil.move(file, path_out)
