import os
import svgwrite
import ast
import math
import cairosvg
from PIL import Image

currdir = os.getcwd() #當前路徑
file_svg = 'test.svg'
output_file = 'output.png'
output_with_transparency = 'output_with_transparency.png'

# 矩形
def draw_rect(drawing, position, size, fill_color='blue', fill_opacity=1):
    # position 起點為矩形左上角
    rect = drawing.rect(insert=position, size=size, fill=fill_color, fill_opacity=fill_opacity)
    drawing.add(rect)

# 圓形
def draw_circle(drawing, position, radius, fill_color='blue', fill_opacity=1):
    # position 圓心座標
    circle = drawing.circle(center=position, r=radius, fill=fill_color, fill_opacity=fill_opacity)
    drawing.add(circle)
# 橢圓
def draw_ellipse(drawing, position, tuple_r, fill_color='blue'):
    # tuple_r = (rx, ry)
    ellipse = drawing.ellipse(center=position, r=tuple_r, fill=fill_color)
    drawing.add(ellipse)

# 多邊形
def draw_polygon(drawing, points, fill_color='black', stroke_color='black', stroke_width=0):
    triangle = drawing.polygon(points=points, fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)
    drawing.add(triangle)

# 扇形
def draw_sector(drawing, center, radius, start_angle, end_angle, fill_color='black', stroke_color='black', stroke_width=0):
    start_x = center[0] + radius * math.cos(math.radians(start_angle))
    start_y = center[1] + radius * math.sin(math.radians(start_angle))
    end_x = center[0] + radius * math.cos(math.radians(end_angle))
    end_y = center[1] + radius * math.sin(math.radians(end_angle))
    large_arc_flag = int(end_angle - start_angle > 180)
    path_data = f"M {center[0]} {center[1]} L {start_x} {start_y} A {radius} {radius} 0 {large_arc_flag} 1 {end_x} {end_y} Z"
    sector = drawing.path(d=path_data, fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)
    drawing.add(sector)

# 轉換連續座標
def create_path_data(points):
    # 連續座標轉換 svg data
    # points:  [(169.282, 140.0), (164.461, 147.379)]
    path_data = f"M {points[0][0]} {points[0][1]}"
    for i in range(1, len(points)):
        path_data += f" L {points[i][0]} {points[i][1]}"
    return path_data

# 曲線
def draw_curve(drawing, points, color='black', width=1):
    for i in range(len(points) - 1):
        segment_path_data = create_path_data([points[i], points[i + 1]])
        curve = drawing.path(d=segment_path_data, stroke=color, stroke_width=width, fill='none')
        drawing.add(curve)
# 文字
def draw_text(drawing, content, position, color='black', size=20, family='Arial', weight=400, style='normal'):
    text = drawing.text(content, insert=position)
    text.update({
        'fill': color,
        'font-size': f'{size}px',
        'font-family': family,
        'font-weight': weight,
        'font-style': style # normal(正常）|italic(斜体）|oblique
    })
    drawing.add(text)


# 轉換透明
def replace_color_with_transparency(image, target_color, threshold=50):
    img = image.convert("RGBA")
    img_data = img.getdata()

    new_img_data = []
    for item in img_data:
        r, g, b, a = item
        if abs(r - target_color[0]) <= threshold and abs(g - target_color[1]) <= threshold and abs(b - target_color[2]) <= threshold:
            new_img_data.append((r, g, b, 0))
        else:
            new_img_data.append(item)

    img.putdata(new_img_data)
    return img

# 調整大小後另存
def resize_and_save(input_path, output_path, tuple_size):
    img = Image.open(input_path)
    resized_img = img.resize(tuple_size)
    resized_img.save(output_path)
    print(f"{input_path} resize saveas finished.")

# 輸出全部
def ouput_all():
    a512 = os.path.join(currdir, 'favicon', 'android-chrome-512x512.png')
    a192 = os.path.join(currdir, 'favicon', 'android-chrome-192x192.png')
    apple_touch = os.path.join(currdir, 'favicon', 'apple-touch-icon.png')
    favicon32 = os.path.join(currdir, 'favicon', 'favicon-32x32.png')
    favicon16 = os.path.join(currdir, 'favicon', 'favicon-16x16.png')
    resize_and_save(output_with_transparency, a512, (512,512))
    resize_and_save(output_with_transparency, a192, (192,192))
    resize_and_save(output_with_transparency, apple_touch, (180,180))
    resize_and_save(output_with_transparency, favicon32, (32,32))
    resize_and_save(output_with_transparency, favicon16, (16,16))
    print("ouput all png finished.")

def svg2png():
    cairosvg.svg2png(url=file_svg, write_to=output_file)
    image = Image.open(output_file)
    target_color = (255, 0, 255) # 指定要替换为透明的颜色
    image_with_transparency = replace_color_with_transparency(image, target_color)
    image_with_transparency.save(output_with_transparency)
    print("Image saved with transparency.")


def scale2(tuple_per, tuple_base):
    # tuple_per 直觀百分比 100%為100 例如 (100, 50) 代表 (1, 0.5)
    # tuple_base 基數 
    a, b = tuple_per
    m, n = tuple_base
    return (a*m*0.01, b*n*0.01)

def scale_points(points, scale=1200/100):
    # 連續座標 依照比例轉換
    return [(round(x*scale,3), round(y*scale,3)) for x, y in points]

def create_svg():
    # 创建SVG图像
    svg_w, svg_h = 1200, 1200
    wh = (svg_w, svg_h)
    dwg = svgwrite.Drawing(file_svg, profile='full', size=(f'{svg_w}px', f'{svg_h}px'))
    transparent = '#ff00ff'

    draw_rect(dwg,
        position = (0, 0),
        size=(svg_w, svg_h),
        fill_color=transparent)

    with open('points.txt', 'r', encoding='utf-8') as f:
        points_string = f.read()
    points = scale_points(ast.literal_eval(points_string))
    draw_polygon(dwg, 
        points=points,
        fill_color='#F80')

    draw_text(dwg,
        content='S',
        position=(svg_w*0.21,svg_h*0.86),
        color='gray',
        size= 0.85*svg_w,
        family='Lucida Bright',
        weight=600,
        style='italic')

    draw_text(dwg,
        content='S',
        position=(svg_w*0.16,svg_h*0.85),
        color='#FFF',
        size= 0.85*svg_w,
        family='Lucida Bright',
        weight=600,
        style='italic')

    dwg.save()
    print("svg saved")

def main():
    create_svg()
    svg2png()
    ouput_all()

def test1():
    with open('points.txt', 'r', encoding='utf-8') as f:
        points_string = f.read()
    print(points_string)
    points = ast.literal_eval(points_string)
    print(points)
    print(type(points))
    for x, y in points:
        print(f'x{x}, y{y}')

if __name__ == '__main__':
    main()