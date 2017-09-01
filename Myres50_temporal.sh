#!bin/sh
python main.py ucf101 Flow ucf101_flow_train_split_1.txt ucf101_flow_val_split_1.txt \
   --arch resnet50 --num_segments 3 \
   --gd 20 --lr 0.001 --lr_steps 190 300 --epochs 340 \
   -b 128 -j 8 \
   --snapshot_pref ucf101_resnet50_ --flow_pref flow_  
