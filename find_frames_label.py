import re
import os
import glob
import json

f = open('label_map.txt')
cat_list = []
while True:
	cat = f.readline()
	if not cat:
		break
	else:
		cat_list.append(cat[:-1])
f.close()
print cat_list

f = file('./kinetics_rgb_val.txt','w')

db_data = json.load(open('./kinetics_splits/kinetics_val.json'))
dir_list = os.listdir('./Kinetics/Val_frames/')
txt = []
i = 1
for dir_name in dir_list:
	print "Processing: {}/{}".format(i,len(dir_list))
	i += 1
	a = db_data[dir_name[:11]]
	b = a['annotations']
	c = b['label']
	c = c.encode("utf-8")
	label = cat_list.index(c)
	img_list = []
	for img in glob.glob('Kinetics/Val_frames/'+dir_name+'/img*'):
		img_list.append(img)
	frame_num = len(img_list)
	if frame_num !=0:
		data_label = 'Kinetics/Val_frames/'+dir_name+' '+str(frame_num)+' '+str(label)+'\n'
		txt.append(data_label)

f.writelines(txt)
f.close()

