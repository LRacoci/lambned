from parser import *

def printTree(tree):
    def printTreeAux(n, tree):
        if type(tree) is not tuple:
            return '  '*n + str(tree)

        resp = ''
        for sub in tree:
            resp += '  '*n  + printTreeAux(n+1,sub) + '\n'

        return resp

    return printTreeAux(0, tree)
  

if __name__ == '__main__':
    parser = Parser()
    from glob import glob
    from itertools import izip
    
    for problem in glob('tests/arq1.hs'):
        print problem
        answer = problem[:-2] + 'res'
        
        with open(problem) as p:
            problem = p.read()
        
        with open(answer) as a:
            answer = a.read()
        
        result = str(parser.parse(problem))
        result = printTree(result)
        if result != answer:
            print result
        else:
            print "ok"
