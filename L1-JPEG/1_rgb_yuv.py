import numpy as np


def RGB2YUV(rgb):
    R = rgb[0]
    G = rgb[1]
    B = rgb[2]
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    Cb = - 0.148 * R - 0.291 * G + 0.439 * B + 128
    Cr = 0.439 * R - 0.368 * G - 0.071 * B + 128
    return [Y, Cb, Cr]


def YUV2RGB(yuv):
    Y = yuv[0]
    Cb = yuv[1]
    Cr = yuv[2]
    R = 1.164 * (Y - 16) + 1.596 * (Cr - 128)
    G = 1.164 * (Y - 16) - 0.813 * (Cr - 128) - 0.391 * (Cb - 128)
    B = 1.164 * (Y - 16) + 2.018 * (Cb - 128)
    return [R, G, B]


while 1:
    print('a) RGB to YUV')
    print('b) YUV to RGB')
    x = str(input())
    if x == 'a':
        rgb = list(map(int, input("\nEnter RGB color: ").strip().split()))[:3]
        print('RGB: ', rgb)
        yuv = RGB2YUV(rgb)
        print('YUV: ', yuv)
        break
    elif x == 'b':
        yuv = list(map(int, input('\nEnter YUV color: ').strip().split()))[:3]
        print('YUV: ', yuv)
        rgb = YUV2RGB(yuv)
        print('RGB: ', rgb)
        break
    else:
        print('\nInvalid option, please select:')
