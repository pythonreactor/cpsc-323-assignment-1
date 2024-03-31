from utils import (
    print_lexical_welcome_banner,
    get_raw_data_from_input,
    get_file_path_from_input,
    get_source_type_from_input
)
from constants import SourceType
from lexical_analyzer import LexicalAnalyzer


def main():
    print_lexical_welcome_banner()

    source_type: SourceType = get_source_type_from_input()

    if source_type == SourceType.File:
        source_file_name: str = get_file_path_from_input()
        analyzer = LexicalAnalyzer(source_type=source_type, source_file_name=source_file_name)
        print(f'Processing file: {source_file_name}', end='\n\n')
    elif source_type == SourceType.Raw:
        source_data = get_raw_data_from_input()
        analyzer = LexicalAnalyzer(source_type=source_type, source_data=source_data)
        print(f'Processing raw data: {source_data}', end='\n\n')
    else:
        raise ValueError(f'Invalid source type: {source_type}')

    analyzer.run()

    # NOTE: We want the max length of a lexeme so we can evenly space the
    # print statements
    max_lexeme_length = max(len(lexeme) for lexeme, _ in analyzer.results)

    print('Set of lexemes and tokens (<lexeme> = <token>)', end='\n\n')
    for lexeme, token in analyzer.results:
        print(f'"{lexeme}"{" " * (max_lexeme_length - len(lexeme))} = {token.value}')
    print(f'Total analyze runtime: {analyzer.total_analyze_runtime:.6f} seconds')


if __name__ == '__main__':
    main()
