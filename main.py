import tkinter as tk

# 读取已知单词列表
with open('list.txt', 'r') as f:
    known_words = [word.strip() for word in f.readlines()]

# 创建主窗口
root = tk.Tk()
root.title('查找未知单词')

# 设置窗口大小和位置
root.geometry('1200x800+300+100')

# 创建左侧输入窗口
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

input_label = tk.Label(input_frame, text='请输入文章：', font=('Arial', 12))
input_label.pack(side=tk.TOP)

input_text = tk.Text(input_frame, width=68, height=50, font=('Arial', 16))
input_text.pack(side=tk.TOP)

# 创建右侧输出窗口
output_frame = tk.Frame(root)
output_frame.pack(side=tk.RIGHT, padx=10, pady=10)

output_label = tk.Label(output_frame, text='文章中的未知单词：', font=('Arial', 12))
output_label.pack(side=tk.TOP)

output_text = tk.Text(output_frame, width=20, height=50, font=('Arial', 16))
output_text.pack(side=tk.TOP)

# 定义查找单词的函数
def find_unknown_words():
    # 获取已知单词列表和输入文章
    known_words = [word.strip() for word in open('list.txt', 'r').readlines()]
    article = input_text.get('1.0', 'end-1c')

    # 将中文标点符号替换为英文标点符号
    article = article.replace('，', ',').replace('。', '.').replace('！', '!').replace('？', '?').replace('；', ';').replace('：', ':').replace('“', '"').replace('”', '"').replace("’", "'")

    # 预处理输入文章中的标点符号
    for char in ',.?!;:"()-1234567890':
        article = article.replace(char, ' ')

    # 分割输入文章为单词列表，并筛选出未出现的单词
    article = article.replace("'s", " is").replace("'ll", " will").replace("'re", " are").replace("'ve", " have").replace("'m", " am").replace("n't", " not").replace("'d", " had")

    # 将所有单词转换为小写字母
    article = article.lower()

    # 分割输入文章为单词列表，并筛选出未出现的单词
    article_words = article.split()
    unknown_words = set([word for word in article_words if word not in known_words])

    # 对未出现的单词进行升序排列
    unknown_words = sorted(list(unknown_words))

    # 在输出窗口中显示未出现的单词
    output_text.delete('1.0', tk.END)
    for word in unknown_words:
        output_text.insert(tk.END, word+'\n')


# 创建查找按钮
find_button = tk.Button(root, text='查找', font=('Arial', 12), command=find_unknown_words)
find_button.pack(side=tk.TOP, pady=100)

# 运行主程序
root.mainloop()