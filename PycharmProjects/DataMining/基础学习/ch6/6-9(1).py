# print
"""
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)#value,.....,表示可以加入无数个参数，
sep=' ',表示表达的时候参数之间以‘ ’空格高隔开，，end='\n',表示结束后换行，所以print（）结束后执行下一个指令就是在下一行了，sep和end都可以
通过关键字参数更改，
"""
print('a' + 'b')#'a' + 'b'是一个参数
print('----'*9)
print('a', 'b')#'a', 'b'是两个参数
print('----'*9)
print('a', 'b', sep='')#之间用空‘’隔开，改变了原来用‘ ’空格隔开的默认情况
print('----'*9)
print('a', 'b', sep='~~')#之间用‘~~’隔开
print('----'*9)
print('a', 'b', end='结束')#结束不再是换行了，而是‘结束’，所以下一个指令是紧接着结束后边的
print('----'*9)
#结果：
# ab
# ------------------------------------
# a b
# ------------------------------------
# ab
# ------------------------------------
# a~~b
# ------------------------------------
# a b结束------------------------------------


