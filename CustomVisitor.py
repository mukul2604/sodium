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

    def visitString(self, ctx):
        return str(ctx.STRING().getText()).strip('\'').strip('\"')

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        try:
            if ctx.op.type == SeawolfGrammarParser.MUL:
                return left * right

            if type(left) == int and type(right) == int:
                return int(left / right)
            else:
                return left / right
        except ZeroDivisionError:
                return "Division by Zero Error"
        except Exception:
            return "SEMANTIC ERROR"

    def visitModulo(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        try:
            if ctx.op.type == SeawolfGrammarParser.MOD:
                return left % right
        except ZeroDivisionError:
            return "Modulo by Zero Error"
        except Exception:
            return "SEMANTIC ERROR"

    def visitExponential(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        try:
            if ctx.op.type == SeawolfGrammarParser.EXP:
                return pow(left, right)
        except Exception:
            return "SEMANTIC ERROR"

    def visitFloorDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        try:
            if ctx.op.type == SeawolfGrammarParser.FLRDIV:
                return left // right
        except ZeroDivisionError:
            return "Floor Division by Zero Error"
        except Exception:
            return "SEMANTIC ERROR"

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        try:
            if ctx.op.type == SeawolfGrammarParser.ADD:
                return left + right
            return left - right
        except Exception:
            return "SEMANTIC ERROR"

    def visitRelational(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        try:
            if type(left) != int or type(right) != int:
                # relation is only for integers here
                raise Exception
            if ctx.op.type == SeawolfGrammarParser.LS:
                return left < right
            if ctx.op.type == SeawolfGrammarParser.GT:
                return left > right
            if ctx.op.type == SeawolfGrammarParser.LE:
                return left <= right
            if ctx.op.type == SeawolfGrammarParser.GE:
                return left >= right
            if ctx.op.type == SeawolfGrammarParser.EQL:
                return left == right
            if ctx.op.type == SeawolfGrammarParser.NE:
                return left != right
            print ("invalid relational operator")
        except Exception:
            return "SEMANTIC ERROR"

    def visitLogicalNOT(self, ctx):
        a = self.visit(ctx.expr())
        try:
            if type(a) != int:
                raise Exception
            return int(not a)
        except Exception:
            return "SEMANTIC ERROR"

    def visitLogical(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        try:
            if type(left) != int or type(right) != int:
                # logical is only for integers here
                raise Exception
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
        except Exception:
            return "SEMANTIC ERROR"

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitList(self, ctx):
        value = self.visit(ctx.listexpr())
        return value

    def visitStringindexing(self, ctx):
        value = self.visit(ctx.expr(0))
        index = self.visit(ctx.expr(1))
        try:
            # if type(value) != str and type(index) != int:
            #     raise Exception
            return value[index]
        except Exception:
            return "SEMANTIC ERROR"

    def visitInoperationstring(self, ctx):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))
        try:
            if value1 in value2:
                return 1
            else:
                return 0
        except Exception:
            return "SEMANTIC ERROR"

