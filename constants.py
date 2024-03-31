from enum import Enum


class SupportedFileType(str, Enum):
    Text = 'txt'


class SourceType(str, Enum):
    File = 'file'
    Raw  = 'raw'


class TokenType(str, Enum):
    Comment    = 'comment'
    Identifier = 'identifier'
    Integer    = 'integer'
    Keyword    = 'keyword'
    Operator   = 'operator'
    Separator  = 'separator'
    Whitespace = 'whitespace'


# NOTE: Order matters - Identifier will pick up a keyword incorrectly if it comes first
REGEX_BY_TOKEN_TYPE = {
    TokenType.Comment   : r'(#.*|//.*|--.*|/\*[\s\S]*?\*/)',
    TokenType.Keyword   : r'\b(class|def|self|if|elif|else|for|pass|continue|break|return|int|float|str|list|AnyStr|List|Dict|Tuple)\b',
    TokenType.Identifier: r'\b[a-zA-Z_]\w*\b',
    TokenType.Integer   : r'\b\d+\b',
    TokenType.Operator  : r'[+|\-|*|/|>|<|=]',
    TokenType.Separator : r'[:;,\(\)\{\}]',
    TokenType.Whitespace: r'\s+'
}
