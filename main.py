import os

# 指定文件夹路径
folder_path = '_posts'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        # 获取不带后缀的文件名
        title = os.path.splitext(filename)[0]
        file_path = os.path.join(folder_path, filename)
        
        # 读取原文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 创建新的内容
        new_content = f'---\ntitle: {title}\n---\n' + content
        
        # 写入新内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("文件处理完成！")
