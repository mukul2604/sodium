from SeawolfGrammarVisitor import SeawolfGrammarVisitor
from SeawolfGrammarParser import SeawolfGrammarParser
import sys


class CustomVisitor(SeawolfGrammarVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        # name = ctx.ID().getText()
        id = ctx.ID()
        if id is not None:
            name = id.getText()
            value = self.visit(ctx.expr())
            self.memory[name] = value
            return value

        name = ctx.listid().ID()[0].getText()
        list_values = self.memory[name]

        try:
            index = int(ctx.listid().INT().getText())
        except Exception:
            index_name = ctx.listid().ID()[1].getText()
            index = self.memory[index_name]

        value = self.visit(ctx.expr())
        list_values[index] = value
        self.memory[name] = list_values
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        # sys.stdout.write(str(value))
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
        return str(ctx.STRING().getText())[1:-1]

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
        result = None

        try:
            if type(left) != int or type(right) != int:
                # relation is only for integers here
                raise Exception
            if ctx.op.type == SeawolfGrammarParser.LS:
                result = left < right
            if ctx.op.type == SeawolfGrammarParser.GT:
                result = left > right
            if ctx.op.type == SeawolfGrammarParser.LE:
                result = left <= right
            if ctx.op.type == SeawolfGrammarParser.GE:
                result = left >= right
            if ctx.op.type == SeawolfGrammarParser.EQL:
                result = left == right
            if ctx.op.type == SeawolfGrammarParser.NE:
                result = left != right
        except Exception:
            return "SEMANTIC ERROR"
        return int(result)

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
            # if type(left) != int or type(right) != int:
            #     # logical is only for integers here
            #     raise Exception
            if ctx.op.type == SeawolfGrammarParser.AND:
                return int(left and right)
            if ctx.op.type == SeawolfGrammarParser.OR:
                return int(left or right)
            print("invalid logical operator")
        except Exception:
            return "SEMANTIC ERROR"

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitIndexing(self, ctx):
        value = self.visit(ctx.expr(0))
        index = self.visit(ctx.expr(1))
        try:
            if type(value) == str:
                value = value[1:-1]
                return "\'" + value[index] + "\'"
            return value[index]
        except Exception:
            return "SEMANTIC ERROR"

    def visitInoperation(self, ctx):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))

        if type(value1) == str and type(value2) == str:
            value1 = value1[1:-1]
            value2 = value2[1:-1]
        try:
            return int(value1 in value2)
            # if value1 in value2:
            #     return 1
            # else:
            #     return 0
        except Exception:
            return "SEMANTIC ERROR"

    def visitList(self, ctx):
        list_visited = []
        start = ctx.listexpr().list_()
        if start.expr() is None:
            return "[]"
        value = self.visit(start.expr())
        if type(value) == str:
            value = value[1:-1]
        list_visited.append(value)
        tail = start.list_()
        while tail is not None:
            value = self.visit(tail.expr())
            if type(value) == str:
                value = value[1:-1]
            list_visited.append(value)
            tail = tail.list_()
        return list_visited

    # not needed to visit block statement explicitly
    # def visitBlockstat(self, ctx:SeawolfGrammarParser.BlockstatContext):
    #     braced_stat = ctx.braced_stat()
    #     self.visit(braced_stat)
    #     # block = braced_stat.block()
    #     # self.visit(block)

    def visitIfstat(self, ctx):
        condition_block = ctx.if_statement().condition_block()
        block_evaluated = int(False)
        for condition in condition_block:
            evaluated = self.visit(condition.expr())

            if evaluated is int(True):
                block_evaluated = evaluated
                self.visit(condition.cond_stat_block())
                break

        if block_evaluated is int(False) and ctx.if_statement().cond_stat_block() is not None:

            self.visit(ctx.if_statement().cond_stat_block())

        return None

    def visitWhilestat(self, ctx):
        while_statement = ctx.while_statement()
        condition_block = while_statement.condition_block()
        guard = self.visit(condition_block.expr())

        while guard is int(True):
            self.visit(condition_block.cond_stat_block())
            guard = self.visit(condition_block.expr())

        return None



