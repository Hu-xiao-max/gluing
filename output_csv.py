import csv
import matplotlib.pyplot as plt
import numpy as np

# 指定CSV文件路径
csv_file_path = 'Contours.csv'
output_csv_path = 'rotated_file.csv'  # 旋转后数据的输出CSV文件路径


def read_and_convert(csv_file_path):
    data = []  


    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:

        csv_reader = csv.reader(file)
        
        for row in csv_reader:

            cleaned_row = [int(x.strip(' []')) for x in row]
            data.append(cleaned_row)
    
    return data


def rotate_coordinates(points, angle, center):

    theta = np.radians(angle)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                 [np.sin(theta), np.cos(theta)]])
    

    rotated_points = []
    for point in points:
        translated_point = np.array(point) - np.array(center)
        rotated_point = rotation_matrix.dot(translated_point)
        rotated_point += np.array(center)
        rotated_points.append(rotated_point)
    
    return rotated_points


converted_data = read_and_convert(csv_file_path)

center_x = np.mean([point[0] for point in converted_data])
center_y = np.mean([point[1] for point in converted_data])
center = (center_x, center_y)

# 旋转角度（例如：45度）
angle = 45
rotated_data = rotate_coordinates(converted_data, angle, center)

# 保存旋转后的数据为CSV文件
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    for point in rotated_data:
        formatted_point = [f"[{int(x)}]" for x in point]
        csv_writer.writerow(formatted_point)


x_coords = [point[0] for point in converted_data]
y_coords = [point[1] for point in converted_data]


rotated_x_coords = [point[0] for point in rotated_data]
rotated_y_coords = [point[1] for point in rotated_data]


plt.figure(figsize=(10, 8))


plt.scatter(x_coords, y_coords, color='blue', label='Original Points', alpha=0.5)


plt.scatter(rotated_x_coords, rotated_y_coords, color='red', label='Rotated Points', alpha=0.5)


plt.scatter(center_x, center_y, color='green', label='Center', zorder=5)

plt.title(f'Pixel Coordinates Visualization (Rotated by {angle} degrees around center)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.axis('equal')  
plt.show()