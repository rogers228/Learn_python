import numpy as np

def calculate_angle_and_direction(A, B):
    # 計算兩個向量的夾角 (0~360 度)
    # A: tuple - 向量 A 的 (x, y) 分量。
    # B: tuple - 向量 B 的 (x, y) 分量。

    # 計算內積與外積
    dot_product = A[0] * B[0] + A[1] * B[1]
    cross_product = A[0] * B[1] - A[1] * B[0]

    # 計算向量的模長
    magnitude_A = np.sqrt(A[0]**2 + A[1]**2)
    magnitude_B = np.sqrt(B[0]**2 + B[1]**2)

    # 計算夾角的餘弦值
    cos_theta = dot_product / (magnitude_A * magnitude_B)
    cos_theta = max(min(cos_theta, 1), -1)  # 限制 cos 值範圍避免數值誤差

    # 計算夾角（弧度）
    angle_rad = np.arccos(cos_theta)

    # 根據外積判斷順時針或逆時針方向
    if cross_product < 0:  # 順時針方向
        clockwise_angle = angle_rad
        counterclockwise_angle = 2 * np.pi - angle_rad
    else:  # 逆時針方向
        counterclockwise_angle = angle_rad
        clockwise_angle = 2 * np.pi - angle_rad

    return {
        # "cw_angle_rad": clockwise_angle,
        # "ccw_angle_rad": counterclockwise_angle,
        "cw_angle_deg": np.degrees(clockwise_angle),
        "ccw_angle_deg": np.degrees(counterclockwise_angle),
    }

def test1():
    A = (33, 20)  # 向量 A
    B = (-18, -20)  # 向量 B

    result = calculate_angle_and_direction(A, B)
    print(result)


if __name__ == '__main__':
    test1()