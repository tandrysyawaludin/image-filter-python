# -- coding: utf-8 --
"""
Created on Wed Jun 23 08:44:20 2021

@author: 
  Kelompok I Pemrograman Komputer C
  Caroline Thalia 6162001150
	Gemala Pavita R 6161801051
	Nanda Fatmawati P 6161801033
"""

import numpy as np
import matplotlib.pyplot as plt
import re
import math

from skimage.io import imread, imshow

# Choose Effect
print("User dapat memilih efek yang akan dipilih, sebagai berikut : ")
quit_res = "N"
effect_type = input("""
+ Manakah efek yang akan anda pilih?

1. Tanpa Efek
2. Penentuan Tepi
3. Mempertajam
4. Pengaburan

Silakan masukkan pilihan Anda: """)

while True:
  if effect_type == "0":
    quit()
  elif not re.match("^[1-4]*$", effect_type) or len(effect_type) > 1 or len(effect_type) < 1:
    effect_type = input("""
Silahkan pilih jawaban dalam bentuk 1 2 3 4 atau 0 untuk keluar
Silakan masukkan pilihan Anda: """)
  else :
    break

# Process Image
image = imread('hamster1.jpg')
plt.figure(num = None, figsize = (6,4), dpi = 100)
imagematrix = np.array(image)
(Nx, Ny, M) = imagematrix.shape
imshow(image)

# Choose Filter Point
filter_point = input("""
+ Pilih titik yang ingin diaplikasikan
------------------------
|      ||      ||      |
|   1  ||   2  ||   3  |
|      ||      ||      |
------------------------
|      ||      ||      |
|   4  ||   5  ||   6  |
|      ||      ||      |
------------------------
|      ||      ||      |
|   7  ||   8  ||   9  |
|      ||      ||      |
------------------------

Pilih nomor daerah yang Anda ingin (1-9) 
atau pilih 0 untuk aplikasi semua titik: """) 

selected_y = 0
selected_x = 0

if filter_point == '1':
  selected_x = 0 
  selected_y = 0
elif filter_point == '2':
  selected_x = math.floor(Ny / 3) 
  selected_y = 0
elif filter_point == '3':
  selected_x = math.floor(2 * Ny / 3) 
  selected_y = 0
elif filter_point == '4':
  selected_x = 0
  selected_y = math.floor(Nx / 3)
elif filter_point == '5':
  selected_x = math.floor(Ny / 3) 
  selected_y = math.floor(Nx / 3)
elif filter_point == '6':
  selected_x = math.floor(2 * Ny / 3) 
  selected_y = math.floor(Nx / 3)
elif filter_point == '7':
  selected_x = 0
  selected_y = math.floor(2 * Nx / 3)
elif filter_point == '8':
  selected_x = math.floor(Ny / 3) 
  selected_y = math.floor(2 * Nx / 3)
elif filter_point == '9':
  selected_x = math.floor(2 * Ny / 3) 
  selected_y = math.floor(2 * Nx / 3)

#ker
if effect_type == '1':
  ker = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype='int')
elif effect_type == '2':
  ker = np.array ([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype='int')
elif effect_type == '3':
  ker = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype='int')
elif effect_type == '4':
  ker = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype='int')
    
#div
div = ker.sum()

if ker.sum() != 0:
  div = ker.sum()
else:
  div = 1

imfill = np.zeros((Nx, Ny, M))

if filter_point == '0':
  for j in range(0,M):
    for baris in range(1,Nx-1):
      for kolom in range(1,Ny-1):
        dummy = 0
        for b in range(-1,2):
          for k in range(-1,2):
            dummy = dummy + image[baris + b][kolom + k][j] * ker[k + 1][b + 1]

        imfill[baris][kolom][j] = math.floor(abs((dummy) / div))
else:
  for j in range(0,M):
    for baris in range(0,Nx): 
      for kolom in range(0,Ny):
        imfill[baris][kolom][j] = image[baris][kolom][j]

  for j in range(0,M):
    for baris in range(selected_y,selected_y + math.ceil(Nx / 3)):
      for kolom in range(selected_x,selected_x + math.ceil(Ny / 3)):
        dummy = 0
        for b in range(-1,2):
          for k in range(-1,2):
            dummy = dummy + image[baris + b][kolom + k][j] * ker[k + 1][b + 1]

        imfill[baris][kolom][j] = math.floor(abs((dummy) / div))

imshow(imfill.astype(np.uint8))
plt.show()
