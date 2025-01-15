import matplotlib.pyplot as plt
import numpy as np


def draw_star(ax, center_x, center_y, radius, angle=0, color='yellow'):
    """
    绘制一个五角星
    :param ax: 绘制的坐标轴
    :param center_x: 星星中心的 x 坐标
    :param center_y: 星星中心的 y 坐标
    :param radius: 星星的外接圆半径
    :param angle: 星星旋转的角度
    :param color: 星星的颜色
    """
    # 计算五角星的顶点坐标
    star_points = []
    for i in range(5):
        outer_x = center_x + radius * np.cos(np.radians(angle + 72 * i))
        outer_y = center_y + radius * np.sin(np.radians(angle + 72 * i))
        inner_x = center_x + radius * 0.382 * np.cos(np.radians(angle + 72 * i + 36))
        inner_y = center_y + radius * 0.382 * np.sin(np.radians(angle + 72 * i + 36))
        star_points.append((outer_x, outer_y))
        star_points.append((inner_x, inner_y))

    # 使用填充多边形绘制五角星
    star_polygon = plt.Polygon(star_points, color=color)
    ax.add_patch(star_polygon)


def draw_china_flag():
    """
    绘制中国国旗
    """
    # 设置国旗的比例 3:2
    flag_width = 15
    flag_height = 10

    # 创建画布
    fig, ax = plt.subplots(figsize=(15, 10))  # 3:2 比例
    # fig, ax = plt.subplots()
    ax.set_xlim(0, flag_width)
    ax.set_ylim(0, flag_height)
    ax.set_aspect('equal')  # 保持长宽比
    ax.axis('off')  # 关闭坐标轴

    # 绘制红色背景
    ax.add_patch(plt.Rectangle((0, 0), flag_width, flag_height, color='red'))

    # 大星星的参数
    big_star_center_x = 2  # 大星星中心位置
    big_star_center_y = 6
    big_star_radius = 1.5

    # 小星星的参数（依次逆时针排列）
    small_star_centers = [
        (4, 7.5),  # 小星星 1
        (5, 6.5),  # 小星星 2
        (5.5, 5),  # 小星星 3
        (5, 3.5)  # 小星星 4
    ]
    small_star_radius = 0.5

    # 绘制大星星
    draw_star(ax, big_star_center_x, big_star_center_y, big_star_radius, angle=0)

    # 绘制小星星（使星星尖朝向大星星中心）
    for center_x, center_y in small_star_centers:
        angle = np.degrees(np.arctan2(big_star_center_y - center_y, big_star_center_x - center_x))
        draw_star(ax, center_x, center_y, small_star_radius, angle)

    # 显示国旗
    plt.show()

    # plt.savefig('draw_picture.png')

# 调用函数绘制国旗
draw_china_flag()
