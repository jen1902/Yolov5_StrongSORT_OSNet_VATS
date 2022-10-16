# Compare image filename and label name (check if an image has missing label)
import os

pathtxt = 'C:/Users/jenni/OneDrive - The Chinese University of Hong Kong/course/2022-23 sem1/BMEG FYP/datasets/VATS/labels_all_10/val'
pathxml = 'C:/Users/jenni/OneDrive - The Chinese University of Hong Kong/course/2022-23 sem1/BMEG FYP/datasets/VATS/labels_all_10_xml/val'

# print all txt label files
listtxt = []
for filename in os.listdir(pathtxt):
    if filename.endswith('.txt'):
        nametxt = filename.rsplit('.', 1)[0]
        listtxt.append(nametxt)
#print(len(listtxt))

# change txt to xml file
listxml=[]
for x in listtxt:
    #print(os.path.join(pathxml+x+'.xml'))
    listxml.append(os.path.join(pathxml+x+'.xml'))
print(len(listxml))

# print currently existing xml file
existxmlfile = []
for filename in os.listdir(pathxml): 
    existxmlfile.append(os.path.join(pathxml+filename))
print(len(existxmlfile))

# check does the xml file exist
for x in listxml:
#     print(x)
#for filename in os.listdir(pathxml): 
    if x not in existxmlfile:
        print(x, 'does not exist')
    




    # else:
    #     print(x, 'dne')
    #print(os.path.join(pathxml+filename))
        # if (x == os.path.join(pathxml+filename)):
        #     print('exisit')
        # else:
        #     print('dne')
        # if os.path.isfile(os.path.join(pathxml+x+'.xml')):
        #     print('file exisit')
        # else:
        #     print(x, 'does not exist')
    # if filename.endswith('.txt'):
    #     nametxt = filename1.rsplit('.', 1)[0]
    #     list.append(nametxt)


