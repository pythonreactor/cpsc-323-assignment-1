import os

import settings
from constants import (
    SupportedFileType,
    SourceType
)

logger = settings.getLogger(__name__)


def exit_program():
    """
    Log and exit the program.
    """
    logger.info('Exiting the program.')
    exit('Goodbye!')


def print_lexical_welcome_banner():
    """
    Print the initial lexical welcome banner to the console.
    """
    print(
        r"""
          _      ________   _______ _____          _
         | |    |  ____\ \ / /_   _/ ____|   /\   | |
         | |    | |__   \ V /  | || |       /  \  | |
         | |    |  __|   > <   | || |      / /\ \ | |
         | |____| |____ / . \ _| || |____ / ____ \| |____
         |______|______/_/ \_\_____\_____/_/____\_\______| _____
             /\   | \ | |   /\   | | \ \   / /___  /  ____|  __ \
            /  \  |  \| |  /  \  | |  \ \_/ /   / /| |__  | |__) |
           / /\ \ | . ` | / /\ \ | |   \   /   / / |  __| |  _  /
          / ____ \| |\  |/ ____ \| |____| |   / /__| |____| | \ \
         /_/    \_\_| \_/_/    \_\______|_|  /_____|______|_|  \_\
        """
    )
    print("Enter 'q' at any time to exit the program.", end='\n\n')


def get_source_type_from_input():
    """
    Retrieve the source type from the user.
    """
    default_selection = SourceType.File

    while True:
        source_type = input(f'Please enter the source type [raw or file] (default {default_selection.value}): ').lower()

        if source_type == settings.MAIN_EXIT_CHAR:
            exit_program()
        elif not source_type:
            return default_selection
        elif source_type not in SourceType:
            print('Invalid source type. Please try again.')
        else:
            break

    return SourceType(source_type)


def get_file_path_from_input():
    """
    Retrieve the file path from the user.
    """
    default_file_path    = 'test_files/initial.txt'
    supported_file_types = ', '.join([file_type.value for file_type in SupportedFileType])

    while True:
        file_path = input(f'Please enter the source file path [supported: {supported_file_types}] (default {default_file_path}): ')

        if file_path == settings.MAIN_EXIT_CHAR:
            exit_program()
        elif not file_path:
            return default_file_path
        elif not file_path:
            print('Invalid file path. Please try again.')
            continue

        extension = file_path.lower().split('.')[-1]
        if extension not in SupportedFileType:
            print('Unsupported file type. Please try again.')
        elif not os.path.isfile(file_path):
            print('File does not exist. Please try again.')
        else:
            break

    return file_path


def get_raw_data_from_input():
    """
    Retrieve the source string.
    """
    source_code = input('Enter your source code: ')

    if source_code == settings.MAIN_EXIT_CHAR:
        exit_program()

    return source_code
