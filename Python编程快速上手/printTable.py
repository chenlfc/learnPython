#! Python3.7
# printTable.py - 编写一个函数，它接受字符串的列表的列表，将它显示在组织良好的表格中
#                 每列右对齐。假定所有内层列表都包含同样数目的字符串。


def printTable(tableData):
    # 检查每行字段的最长长度并保存在格式列表中
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for v in tableData[i]:
            if len(v) > colWidths[i]:
                colWidths[i] = len(v)
    # 按格式输出列表内容
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j == 0:
                print(tableData[j][i].rjust(colWidths[j]), end=' ')
            else:
                print(tableData[j][i].ljust(colWidths[j]), end=' ')
        print()
    print(colWidths)


tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
    ['dogs', 'cats', 'moose', 'goose']
]
printTable(tableData)
