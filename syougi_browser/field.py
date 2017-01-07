#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Field(object):
  field = [[[0 for k in range(1)] for j in range(9)] for i in range(9)]
  rfield = [0 for r in range(81)]
  komastr = ["--・","▼歩","▼香","▼桂","▼銀","▼金","▼角","▼飛","▼王",
             "▼と","▼杏","▼圭","▼全","▼金","▼馬","▼竜",
             "--・","△歩","△香","△桂","△銀","△金","△角","△飛","△玉",
             "△と","△杏","△圭","△全","△金","△馬","△竜"]

  def start(self):
    for i in range(0,9):
      if (i <= 2):
        ch = 0
      elif (i >= 6):
        ch = 16
      for j in range(0,9):
        if (i == 0 or i == 8):
          if (j == 0 or j == 8):
            Field.field[i][j] = 2 + ch
          elif (j == 1 or j == 7):
            Field.field[i][j] = 3 + ch
          elif (j ==2 or j == 6):
            Field.field[i][j] = 4 + ch
          elif (j == 3 or j == 5):
            Field.field[i][j] = 5 + ch
          elif (j == 4):
            Field.field[i][j] = 8 + ch
        elif (i == 1):
          if (j == 1):
            Field.field[i][j] = 6
          elif (j == 7):
            Field.field[i][j] = 7
          else:
            Field.field[i][j] = 0 + ch
        elif(i == 7):
          if (j == 1):
            Field.field[i][j] = 23
          elif (j == 7):
            Field.field[i][j] = 22  
          else:
            Field.field[i][j] = 0 + ch
        elif (i == 2 or i == 6):
          Field.field[i][j] = 1 + ch
        else:
          Field.field[i][j] = 0 + ch
    print("finish")

  def seiretu(self):
    cnt = 0
    for i in range(0,9):
      for j in range(0,9):
        Field.rfield[cnt] = Field.field[i][j]
        cnt += 1