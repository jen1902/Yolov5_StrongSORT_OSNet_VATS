# Rename files
import os

path = 'E:/Datasets/VATS/images_split/knotpusher_grasper'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'knotpusher_grasper_'+str(i)+'.jpg'))
    i = i +1