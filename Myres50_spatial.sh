#!bin/sh
python main.py ucf101 RGB ucf101_rgb_train_split_1.txt ucf101_rgb_val_split_1.txt \
   --arch resnet50 --num_segments 3 \
   --gd 20 --lr 0.001 --lr_steps 30 60 --epochs 80 \
   -b 128 -j 8 \
   --snapshot_pref ucf101_resnet50_ 
