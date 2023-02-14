from pathlib import Path
from NGram import NGram

file = open("data/CVPR2021/CVPR2021.txt", "r", encoding='UTF8')

lines = file.readlines()


final = []

for i in range(len(lines)):
    lines[i].strip('\n')
    
print(len(lines))
