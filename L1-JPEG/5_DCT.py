# Source: https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from numpy import r_
from scipy import signal
from scipy import misc
import matplotlib.pylab as pylab
from pathlib import Path


# 2D DCT function
def DCT_2D(a):
    return scipy.fftpack.dct(scipy.fftpack.dct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


# 2D IDCT function
def IDCT_2D(a):
    return scipy.fftpack.idct(scipy.fftpack.idct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


# Perform a blockwise DCT
def dct_transform(im, block_size):
    dct = np.zeros(im.shape)
    for i in r_[:im.shape[0]:block_size]:
        for j in r_[:im.shape[1]:block_size]:
            dct[i:(i+block_size), j:(j+block_size)
                ] = DCT_2D(im[i:(i+block_size), j:(j+block_size)])
    return dct


def idct_transform(dct, block_size):
    idct = np.zeros(dct.shape)
    for i in r_[:dct.shape[0]:block_size]:
        for j in r_[:dct.shape[1]:block_size]:
            idct[i:(i+block_size), j:(j+block_size)
                 ] = IDCT_2D(dct_thresh[i:(i+block_size), j:(j+block_size)])
    return idct


input_path = Path.cwd()
input_file = str(input_path / "lenna.jpg")

print('Enter the block size of the DCT (i.e: 4, 8, 16, 32)')
block_size = int(input())

output_path = Path.cwd() / "Results/5-DCT"
output_path.mkdir(parents=True, exist_ok=True)
output_file1 = str(output_path / "DCT_coefficients_bs") + \
    str(block_size) + ".jpg"
output_file2 = str(output_path / "Original_DCT_bs") + str(block_size) + ".jpg"


im = plt.imread(input_file).astype(float)
dct = dct_transform(im, block_size)

# Display all DCT blocks
plt.figure()
plt.imshow(dct, cmap='gray', vmax=np.max(dct)*0.01, vmin=0)
plt.title(str(block_size) + "x" + str(block_size) + " DCTs of the image")
plt.savefig(output_file1)
plt.show()

# Threshold DCT coefficients
thresh = 0.012
dct_thresh = dct * (abs(dct) > (thresh*np.max(dct)))
percent_nonzeros = np.sum(dct_thresh != 0.0) / (im.shape[0]*im.shape[1]*1.0)
print("Keeping only %f%% of the DCT coefficients" % (percent_nonzeros*100.0))

idct = idct_transform(dct_thresh, block_size)

# Compare DCT compressed image with original
plt.figure()
plt.imshow(idct, cmap='gray')
plt.title("DCT compressed image")
plt.savefig(output_file2)
plt.show()
