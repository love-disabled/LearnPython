#square function with memory
def square():
    memory = {}

    def inner(x):
        if x in memory:
            print("in memory")
            return memory[x]
        else:
            print("not in memory")
            sq = x*x
            memory[x] = sq
            return memory[x]
    return inner

function = square()
#line16:创建def square的 local frame
#定义字典memory = {}
#定义内部函数inner(x)
#返回inner 赋值给global frame的function
print(function(3))
print(function(5))
print(function(5))
#frame查找是local->enclosing->global
#closure可以outer传入一个参数固定函数用途，如累加5