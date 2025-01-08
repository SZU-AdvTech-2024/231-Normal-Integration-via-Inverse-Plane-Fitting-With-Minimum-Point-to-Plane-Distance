import numpy as np
import imageio
import os

def png_to_npy(png_file, npy_file):
    img = imageio.imread(png_file)
    mask = np.sum(img, axis = -1, keepdims = True) > 0
    img = (img / 255. * 2 - 1) * mask
    np.save(npy_file, {'normal_map': img, 'mask': mask})

if __name__ == '__main__':
    for root, dir, files in os.walk("data/my_data"):
        for file in files:
            if file.endswith(".png"):
                norm_path = os.path.join(root, file)
                print(norm_path)
                npy_path = os.path.join(root, file.replace(".png", ".npy"))
                png_to_npy(norm_path, npy_path)