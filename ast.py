variables = {}

# class Null:
#     def eval(self):
#         return self

#     def getstr(self):
#         return 'NULL'
    
# class Statements:
#     def __init__(self, nodes):
#         self .nodes = nodes

#     def eval(self):
#         for node in self.nodes:
#             node.eval()
    
class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)
    
# class Int():
#     def __init__(self, value):
#         self.value = value

#     def eval(self):
#         return int(self.value)
    
# class Real():
#     def __init__(self, value):
#         self.value = value

#     def eval(self):
#         return float(self.value)
    
# class String:
#     def __init__(self, value):
#         self.value = value

#     def eval(self):
#         return str(self.value[1:-1])
    
class Bool:
    def __init__(self, value):
        self.value = value

    def eval(self):
        if (self.value):
            return "true"
        else:
            return "false"


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()
      
class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

#Operadores Relacionales   
class BinOp:
    def __init__(self, left, binop, right):
        self.left = left
        self.binop = binop
        self.right = right

    def eval(self):
        if self.binop == "EQ":
            return Bool(self.left.eval() == self.right.eval()).eval()
        elif self.binop == "NOTEQ":
            return Bool(self.left.eval() != self.right.eval()).eval()
        elif self.binop == "GRE":
            return Bool(self.left.eval() > self.right.eval()).eval()
        elif self.binop == "LESS":
            return Bool(self.left.eval() < self.right.eval()).eval()
        elif self.binop == "GRETH":
            return Bool(self.left.eval() >= self.right.eval()).eval()
        elif self.binop == "LESSTH":
            return Bool(self.left.eval() <= self.right.eval()).eval()
        else:
            raise AssertionError("Something went super wrong.")

# class If:
#     def __init__(self, condition, body, else_body=None):
#         self.condition = condition
#         self.body = body
#         self.else_body = else_body

#     def eval(self):
#         if self.condition.eval() == "true":
#             return self.body.eval()
#         elif self.else_body is not None:
#             return self.else_body.eval()
#         return Null()

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())