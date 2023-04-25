from rply import ParserGenerator
from ast import Number, Sum, Sub, Mul, Div, Print, Bool, BinOp


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV',
            'BOOL', 'GRE', 'LESS', 'GRETH', 'LESSTH', 'EQ', 'NOTEQ'],

             precedence= [
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV'])
             ]
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            
        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def exp_paren(p):
            return p[1]
        
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)
        #Operadores Relacionales
        # @self.pg.production('expression : REAL_VAL')
        # @self.pg.production('expression : INT_VAL')
        # def number(p):
        #     if (p[0].gettokentype() == 'REAL_VAL'):
        #         return Real(p[0].value)
        #     return Number(p[0].value)
        
        # @self.pg.production('expression : STRING_VAL')
        # def string(p):
        #     return String(p[0].value[1:-1])
        
        @self.pg.production('expression : expression LESS expression')
        def less(p):
            return BinOp(p[0], "LESS", p[2])
        
        @self.pg.production('expression : expression GRE expression')
        def greater(p):
            return BinOp(p[0], "GRE", p[2])
        
        @self.pg.production('expression : expression GRETH expression')
        def greaterThan(p):
            return BinOp(p[0], "GRETH", p[2])
        
        @self.pg.production('expression : expression LESSTH expression')
        def greaterThan(p):
            return BinOp(p[0], "LESSTH", p[2])
        
        @self.pg.production('expression : expression EQ expression')
        def equal(p):
            return BinOp(p[0], "EQ", p[2])
        
        @self.pg.production('expression : expression NOTEQ expression')
        def notEqual(p):
            return BinOp(p[0], "NOTEQ", p[2])
        
        # # String
        # @self.pg.production('expression : STRING')
        # def exp_string(p):
        #     return String(p[0].getstr())
        
        # Bool
        @self.pg.production('expression : BOOL')
        def exp_boolean(p):
            if p[0].getstr() == "true":
                return Bool(True)
            else:
                return Bool(False)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()