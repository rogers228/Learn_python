from tool_draw import *

def test1():
    arc = calculate_points_on_arc(
    center = (50, 14),
    radius = 14,
    start_angle = -180,
    end_angle = 0,
    num_points = 12);
    # print(arc)
    points2draw(arc)

def test2():
    # 中空
    g_bw = 5 # border
    g_r = 10 # radius
    g_r_num = 10
    ps = []
    
    line = [(50,0),(0,0),(0,50),(0+g_bw,50),(0+g_bw,g_bw+g_r)]; line.pop(); ps += line
    # print(line)
    arc = calculate_points_on_arc(
    center = (g_bw+g_r, g_bw+g_r),
    radius = g_r,
    start_angle = 180,
    end_angle = 180+90,
    num_points = g_r_num); arc.pop(); ps += arc
    
    line = [(g_bw+g_r, g_bw),(50,g_bw),(100-g_bw-g_r,g_bw)]; line.pop(); ps += line

    arc = calculate_points_on_arc(
    center = (100-g_bw-g_r, g_bw+g_r),
    radius = g_r,
    start_angle = 270,
    end_angle = 270+90,
    num_points = g_r_num); arc.pop(); ps += arc

    line = [(100-g_bw, g_bw+g_r),(100-g_bw, 50),(100,50),(100,0),(50,0)] ; ps += line
    # print(ps)
    polygon_str = ','.join([f'{p[0]}% {p[1]}%' for p in ps])
    print(polygon_str)


    points2draw(ps)


if __name__ == '__main__':
    test2()