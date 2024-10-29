import csv
import matplotlib.pyplot as plt
import numpy as np

# 指定CSV文件路径
csv_file_path = '/home/hu/research/gluing/Contours.csv'

# 读取CSV文件并转换数据
def read_and_convert(csv_file_path):
    data = []  # 存储转换后的数据

    # 打开CSV文件
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        # 创建一个csv.reader对象
        csv_reader = csv.reader(file)
        
        # 遍历CSV文件中的每一行
        for row in csv_reader:
            # 使用列表推导式去除每行中的'[', ']', 空格，并转换为整数
            cleaned_row = [int(x.strip(' []')) for x in row]
            # 将清洗后的数据添加到data列表中
            data.append(cleaned_row)
    
    return data

# 旋转坐标
def rotate_coordinates(points, angle, center):
    # 将角度转换为弧度
    theta = np.radians(angle)
    # 旋转矩阵
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                 [np.sin(theta), np.cos(theta)]])
    
    # 旋转每个点
    rotated_points = []
    for point in points:
        # 将点平移到中心点
        translated_point = np.array(point) - np.array(center)
        # 应用旋转矩阵
        rotated_point = rotation_matrix.dot(translated_point)
        # 将点平移回原位置
        rotated_point += np.array(center)
        rotated_points.append(rotated_point)
    
    return rotated_points

# 调用函数并获取数据
converted_data = read_and_convert(csv_file_path)

# 计算中心点坐标
center_x = np.mean([point[0] for point in converted_data])
center_y = np.mean([point[1] for point in converted_data])
center = (center_x, center_y)

# 提取x和y坐标
x_coords = [point[0] for point in converted_data]
y_coords = [point[1] for point in converted_data]

# 旋转角度（例如：45度）
angle = 45
rotated_data = rotate_coordinates(converted_data, angle, center)

# 提取旋转后的x和y坐标
rotated_x_coords = [point[0] for point in rotated_data]
rotated_y_coords = [point[1] for point in rotated_data]

# 可视化原始坐标和旋转后的坐标
plt.figure(figsize=(10, 8))

# 绘制原始坐标
plt.scatter(x_coords, y_coords, color='blue', label='Original Points', alpha=0.5)

# 绘制旋转后的坐标
plt.scatter(rotated_x_coords, rotated_y_coords, color='red', label='Rotated Points', alpha=0.5)

# 绘制中心点
plt.scatter(center_x, center_y, color='green', label='Center', zorder=5)

plt.title(f'Pixel Coordinates Visualization (Rotated by {angle} degrees around center)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.axis('equal')  # 保持比例
plt.show()