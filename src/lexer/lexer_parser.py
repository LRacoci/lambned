import purplex as lp


class Lexer(lp.Lexer):

    MAIN = lp.TokenDef(r'main')
    DEFINITION = lp.TokenDef(r':=')

    LPAREN = lp.TokenDef(r'\(')
    RPAREN = lp.TokenDef(r'\)')
    
    NEWLINE = lp.TokenDef(r'\n')

    INTEGER = lp.TokenDef(r'\d+')

    TIMES = lp.TokenDef(r'\*')
    DIVIDE = lp.TokenDef(r'/')
    PLUS = lp.TokenDef(r'\+')
    MINUS = lp.TokenDef(r'-')

    BOOLEAN = lp.TokenDef(r'(True)|(False)')

    AND = lp.TokenDef(r'and')
    NOT = lp.TokenDef(r'not')
    OR  = lp.TokenDef(r'or')






    WHITESPACE = lp.TokenDef(r'[\s]+', ignore=True)




class Parser(lp.Parser):

    LEXER = Lexer
    START = 'start'
    EXPRESSION = 'expression'

    PRECEDENCE = (
        (lp.LEFT, 'UMINUS'),
        (lp.LEFT, 'TIMES', 'DIVIDE'),
        (lp.LEFT, 'PLUS', 'MINUS'),
    )
    @lp.attach('start : MAIN DEFINITION expression')
    def main(self,  definition, main, expr):
        return expr
    
    @lp.attach('expression : INTEGER')
    def number(self, num):
        return int(num)
    
    @lp.attach('expression : LPAREN expression RPAREN')
    def brackets(self, lparen, expr, rparen):
        return expr

    @lp.attach('expression : PLUS expression expression')
    def addition(self, op, left, right):
        return left + right

    @lp.attach('expression : MINUS expression expression')
    def subtract(self, op, left, right):
        return left - right

    @lp.attach('expression : TIMES expression expression')
    def multiply(self, op, left, right):
        return left * right

    @lp.attach('expression : DIVIDE expression expression')
    def division(self, op, left, right):
        return left / right
    @lp.attach('expression : MINUS expression', prec_symbol='UMINUS')
    def negate(self, minus, expr):
        return -expr
    """
    """

if __name__ == '__main__':
    parser = Parser()
    problems = [
        ('main := + 2 - * 3 4 4', 10),
        ('main := *(-2)-(+ 1 1)', 4),
        ('main := - * / 6 2 4 * 8 1', 4),
    ]
    for problem, answer in problems:
        result = parser.parse(problem)
        print result == answer