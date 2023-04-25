from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parentesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Brackets
        self.lexer.add('OPEN_BR', r'\{')
        self.lexer.add('CLOSE_BR', r'\}')
        # Comment
        self.lexer.add('COMMENT', r'\#')
        # Simbolos
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('DOT', r'\.')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('QUOTE', r'\"')
        self.lexer.add('DOUBLEC', r'::')
        # Operadores Aritmeticos
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        # Operadores Relacionales
        self.lexer.add('GRETH', r'>=')
        self.lexer.add('LESSTH', r'<=')
        self.lexer.add('LESS', r'\<')
        self.lexer.add('GRE', r'\>')
        self.lexer.add('NOTEQ', r'!=')
        self.lexer.add('EQ', r'==')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')
        #Palabras Reservadas
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('THEN', r'then')
        self.lexer.add('DO', r'do')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('END', r'end')
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        self.lexer.add('INT', r'int')
        self.lexer.add('STRING', r'string')
        self.lexer.add('REAL', r'real')
        self.lexer.add('BOOL', r'bool')
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        self.lexer.add('FOR', r'for')
        self.lexer.add('MAIN', r'main')
        #Equal
        self.lexer.add('EQUAL', r'\=')
        #Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()