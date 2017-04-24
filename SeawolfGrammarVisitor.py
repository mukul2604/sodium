# Generated from /Users/mukul/github/sodium/SeawolfGrammar.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SeawolfGrammarParser import SeawolfGrammarParser
else:
    from SeawolfGrammarParser import SeawolfGrammarParser

# This class defines a complete generic visitor for a parse tree produced by SeawolfGrammarParser.

class SeawolfGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SeawolfGrammarParser#prog.
    def visitProg(self, ctx:SeawolfGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#code_block.
    def visitCode_block(self, ctx:SeawolfGrammarParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#printExpr.
    def visitPrintExpr(self, ctx:SeawolfGrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#assign.
    def visitAssign(self, ctx:SeawolfGrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#ifstat.
    def visitIfstat(self, ctx:SeawolfGrammarParser.IfstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#whilestat.
    def visitWhilestat(self, ctx:SeawolfGrammarParser.WhilestatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#blockstat.
    def visitBlockstat(self, ctx:SeawolfGrammarParser.BlockstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#blank.
    def visitBlank(self, ctx:SeawolfGrammarParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#while_statement.
    def visitWhile_statement(self, ctx:SeawolfGrammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#if_statement.
    def visitIf_statement(self, ctx:SeawolfGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#condition_block.
    def visitCondition_block(self, ctx:SeawolfGrammarParser.Condition_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#cond_stat_block.
    def visitCond_stat_block(self, ctx:SeawolfGrammarParser.Cond_stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#braced_statement.
    def visitBraced_statement(self, ctx:SeawolfGrammarParser.Braced_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#parens.
    def visitParens(self, ctx:SeawolfGrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Inoperation.
    def visitInoperation(self, ctx:SeawolfGrammarParser.InoperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#string.
    def visitString(self, ctx:SeawolfGrammarParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#MulDiv.
    def visitMulDiv(self, ctx:SeawolfGrammarParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#AddSub.
    def visitAddSub(self, ctx:SeawolfGrammarParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Modulo.
    def visitModulo(self, ctx:SeawolfGrammarParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Relational.
    def visitRelational(self, ctx:SeawolfGrammarParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#negreal.
    def visitNegreal(self, ctx:SeawolfGrammarParser.NegrealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Logical.
    def visitLogical(self, ctx:SeawolfGrammarParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Exponential.
    def visitExponential(self, ctx:SeawolfGrammarParser.ExponentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#negint.
    def visitNegint(self, ctx:SeawolfGrammarParser.NegintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#real.
    def visitReal(self, ctx:SeawolfGrammarParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#FloorDiv.
    def visitFloorDiv(self, ctx:SeawolfGrammarParser.FloorDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#list.
    def visitList(self, ctx:SeawolfGrammarParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#int.
    def visitInt(self, ctx:SeawolfGrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#LogicalNOT.
    def visitLogicalNOT(self, ctx:SeawolfGrammarParser.LogicalNOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#id.
    def visitId(self, ctx:SeawolfGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#Indexing.
    def visitIndexing(self, ctx:SeawolfGrammarParser.IndexingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#listid.
    def visitListid(self, ctx:SeawolfGrammarParser.ListidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#list_index.
    def visitList_index(self, ctx:SeawolfGrammarParser.List_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#listexpr.
    def visitListexpr(self, ctx:SeawolfGrammarParser.ListexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#list_.
    def visitList_(self, ctx:SeawolfGrammarParser.List_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfGrammarParser#empty_list.
    def visitEmpty_list(self, ctx:SeawolfGrammarParser.Empty_listContext):
        return self.visitChildren(ctx)



del SeawolfGrammarParser