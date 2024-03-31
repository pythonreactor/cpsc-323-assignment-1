import os
import re
import time
from typing import (
    List,
    Tuple
)
from dataclasses import (
    field,
    dataclass
)

from constants import (
    SourceType,
    TokenType,
    REGEX_BY_TOKEN_TYPE
)


@dataclass
class LexicalAnalyzer:
    """
    Lexical Analyzer class that can analyze source data that
    is either in a file or raw data.
    """
    source_type: SourceType
    source_file_name: str = None
    source_data: str      = None

    results: List[Tuple[TokenType, str]] = field(default_factory=list)
    total_analyze_runtime: float         = 0.0

    def _get_content_from_file(self) -> str:
        """
        Read the content from the source data file (if applicable).
        """
        with open(self.source_file_name, 'r') as file:
            content = file.read()

        return content

    def analyze_content(self):
        """
        Run a lexical analysis on the content of the source data.
        """
        _start = time.time()

        data = self.source_data
        data = re.sub(REGEX_BY_TOKEN_TYPE[TokenType.Comment], '', data)

        while data:
            re_match = None

            for token, re_pattern in REGEX_BY_TOKEN_TYPE.items():
                regex = re.compile(re_pattern)
                re_match = regex.match(data)

                if re_match:
                    # NOTE: We still need to find the whitespaces so we can
                    # remove them from the data string; we just don't want
                    # to add them to our results.
                    if token != TokenType.Whitespace:
                        lexeme = re_match.group()
                        self.results.append((lexeme, token))

                    data = data[re_match.end():]
                    break

            if not re_match:
                raise SyntaxError(f'Unknown token: {data[0]}')

        self.total_analyze_runtime = time.time() - _start

    def run(self):
        if self.source_type not in SourceType:
            raise ValueError(f'Invalid source type: {self.source_type}')

        if self.source_type == SourceType.File:
            if not os.path.isfile(self.source_file_name):
                raise FileNotFoundError(f'File not found: {self.source_file_name}')

            self.source_data = self._get_content_from_file()

        self.analyze_content()
