def get_even_squares(num_list):
    #題目要求 : 使用列表推導式(List Comprehension)
    #接收整數列表
    #傳回所有偶數的平方值的列表(奇數不計算和不加入列表)
    return [num**2 for num in num_list if num%2==0]

def get_odd_cubes(num_list):
    #題目要求 : 使用迴圈
    #接收整數列表
    #傳回奇數的 3 次方值列表(偶數不計算和不加入列表)
    lis = []                                #建立一個臨時列表
    for num in num_list:                    #迴圈將傳入的串列照順序取出
        if(num%2==1):                       #整數除2的餘數等於1為奇數
            lis.append(num**3)              #將整數做3次方計算後加入臨時列表
    return lis                              #回傳完成的臨時陣列

def get_sliced_list(num_list):
    #題目要求 : 使用切片
    #接收整數列表
    #傳回從第 5 個元素開始到最後一個元素(包含最後一個)的列表
    return num_list[4:]                     #傳回第5個元素到最後一個元素的列表

def format_numbers(numbers):
    #題目要求 : 將列表中的每個數字都格式化為8個字元的寬度，並靠右對齊
    #接收整數列表
    #傳回字串列表
    lis = []                                #建立一個臨時列表
    for var in numbers:                     #迴圈將傳入的串列照順序取出
        lis.append("{:>8d}".format(var))    #使用format，8個字元寬度和向右對齊，最後將值加入臨時列表
    return lis                              #傳回臨時列表

def main():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]      #測試用的整數列表

    even_lis =  get_even_squares(num_list)      #偶數的平方值(整數列表)
    odd_lis = get_odd_cubes(num_list)           #奇數的三次方值(整數列表)
    slic_lis = get_sliced_list(num_list)        #第5個元素到最後一個元素(整數列表)

    #整理列表內的值，8個字元寬度和像右對齊
    format_even = format_numbers(even_lis)      #偶數的平方值列表格式化為8個字元的寬度,並靠右對齊(字串列表)
    format_odd = format_numbers(odd_lis)        #奇數的三次方值列表格式化為8個字元的寬度,並靠右對齊(字串列表)
    format_slic = format_numbers(slic_lis)      #第5個元素到最後一個元素列表格式化為8個字元的寬度,並靠右對齊(字串列表)

    #搭配print() 與 join() 顯示最後結果
    symbol = ','                                #使用','做為分隔符號
    print(symbol.join(format_even))             #join將列表的值和分隔符號連接
    print(symbol.join(format_odd))
    print(symbol.join(format_slic))

if __name__ == "__main__":
    main()
