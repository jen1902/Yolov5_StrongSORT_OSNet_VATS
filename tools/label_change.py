# Change labelling (rename into a new label format/ change class name or number of classes)
import os

path = 'C:/Users/jenni/OneDrive - The Chinese University of Hong Kong/course/2022-23 sem1/BMEG FYP/datasets/VATS/labels_all_14/train'
path_s = 'C:/Users/jenni/OneDrive - The Chinese University of Hong Kong/course/2022-23 sem1/BMEG FYP/datasets/VATS/labels_all_11/train'

# path = 'D:\Datasets\VATS\labels_split_class\clamp_o_rl'
# path_s = 'D:\Datasets\VATS\labels_split_class\clamp_o_rl_copy'
prefixed = [filename for filename in os.listdir(path) if filename.startswith("suction")]
#print(prefixed)


i = 0
for name in prefixed:
    filename = os.path.join(path,  name)
    filename_s = os.path.join(path_s,  name)
    with open(filename, 'r') as f:
        new_txt = []
        lines = f.readlines()
        for line in lines:
            #print(line[:-1])
            split = line[:-1].split()
            # if (split[0] == '5' or split[0] == '6'):
            split[0] = '8'
            #print(split)
            new_str = " ".join(split)
            #print(new_str)
            new_str = new_str + "\n"
            new_txt.append(new_str)
        print('The new str: ', filename_s, new_txt)
        with open(filename_s, 'w') as f:
             f.writelines(new_txt)
    i += 1
print('Total number of files', i)
