import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_folder(folderpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folderpath))


if "{{cookiecutter.open_source_license}}" == "No license file":
    remove_file("LICENSE")
