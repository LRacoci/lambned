from lexer import *
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
    def main(self,  main, definition, expr):
        return 'main', (expr)

    @lp.attach('expression : INTEGER')
    def number(self, num):
        return int(num)
    
    @lp.attach('expression : LPAREN expression RPAREN')
    def brackets(self, lparen, expr, rparen):
        return '(', (expr), ')'

    @lp.attach('expression : expression PLUS expression')
    def addition(self, left, op, right):
        return '+', left, right

    @lp.attach('expression : expression MINUS expression')
    def subtract(self, left, op, right):
        return '-', left, right

    @lp.attach('expression : expression TIMES expression')
    def multiply(self, left, op, right):
        return '*', left, right

    @lp.attach('expression : expression DIVIDE expression')
    def division(self, left, op, right):
        return '/', left, right
	
    @lp.attach('expression : MINUS expression', prec_symbol='UMINUS')
    def negate(self, minus, expr):
        return '-', expr
