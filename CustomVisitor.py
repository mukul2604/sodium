from SeawolfGrammarVisitor import SeawolfGrammarVisitor
from SeawolfGrammarParser import SeawolfGrammarParser


class CustomVisitor(SeawolfGrammarVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitReal(self, ctx):
        return float(ctx.REAL().getText())

    def visitNegreal(self, ctx):
        return -float(ctx.REAL().getText())

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitNegint(self, ctx):
        return -int(ctx.INT().getText())

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == SeawolfGrammarParser.MUL:
            return left * right
        try:
            if type(left) == int and type(right) == int:
                return int(left / right)
            else:
                return left / right
        except ZeroDivisionError:
            return "Division by Zero error"

    def visitModulo(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == SeawolfGrammarParser.MOD:
            try:
                return left % right
            except ZeroDivisionError:
                return "Modulo by Zero error"

    def visitExponential(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfGrammarParser.EXP:
            return pow(left, right)

    def visitFloorDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfGrammarParser.FLRDIV:
            return left // right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == SeawolfGrammarParser.ADD:
            return left + right
        return left - right

    def visitRelational(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == SeawolfGrammarParser.LS:
            return int(left < right)
        if ctx.op.type == SeawolfGrammarParser.GT:
            return int(left > right)
        if ctx.op.type == SeawolfGrammarParser.LE:
            return int(left <= right)
        if ctx.op.type == SeawolfGrammarParser.GE:
            return int(left >= right)
        if ctx.op.type == SeawolfGrammarParser.EQL:
            return int(left == right)
        if ctx.op.type == SeawolfGrammarParser.NE:
            return int(left != right)
        print ("invalid relational operator")

    def visitLogicalNOT(self, ctx):
        a = self.visit(ctx.expr())
        return int(not int(a))

    def visitLogical(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == SeawolfGrammarParser.AND:
            if left and right:
                return 1
            else:
                return 0
        if ctx.op.type == SeawolfGrammarParser.OR:
            if left or right:
                return 1
            else:
                return 0
        print("invalid logical operator")

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitMylist(self, ctx):
        return self.visit(ctx.elems())
