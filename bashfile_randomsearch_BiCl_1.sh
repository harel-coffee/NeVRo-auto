#!/usr/bin/env bash

# Random Search Bashfile_1: classification
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 65,10 --fc_n_hidden 0 --learning_rate 5e-4 --weight_reg l2 --weight_reg_strength 1.44 --activation_fct elu --filetype SSD --hilbert_power True --band_pass False--component 1,2,3,5,6,7 --hrcomp True --path_specificities BiCl_RndHPS_lstm-65-10_fc-0_lr-5e-4_wreg-l2-1.44_actfunc-elu_ftype-SSD_hilb-T_bpass-F_comp-1-2-3-5-6-7_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30,30 --fc_n_hidden 10 --learning_rate 5e-4 --weight_reg l2 --weight_reg_strength 0.72 --activation_fct elu --filetype SSD --hilbert_power False --band_pass False--component best --hrcomp True --path_specificities BiCl_RndHPS_lstm-30-30_fc-10_lr-5e-4_wreg-l2-0.72_actfunc-elu_ftype-SSD_hilb-F_bpass-F_comp-best_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 50 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l2 --weight_reg_strength 0.18 --activation_fct relu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp True --path_specificities BiCl_RndHPS_lstm-50_fc-0_lr-1e-2_wreg-l2-0.18_actfunc-relu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 25,20 --fc_n_hidden 15 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct relu --filetype SSD --hilbert_power False --band_pass True--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-25-20_fc-15_lr-1e-2_wreg-l1-0.36_actfunc-relu_ftype-SSD_hilb-F_bpass-T_comp-best_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 25 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 1e-05 --activation_fct elu --filetype SSD --hilbert_power False --band_pass True--component 1 --hrcomp True --path_specificities BiCl_RndHPS_lstm-25_fc-0_lr-1e-2_wreg-l1-0.00_actfunc-elu_ftype-SSD_hilb-F_bpass-T_comp-1_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 80 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct elu --filetype SSD --hilbert_power False --band_pass False--component best --hrcomp True --path_specificities BiCl_RndHPS_lstm-80_fc-0_lr-1e-2_wreg-l1-0.36_actfunc-elu_ftype-SSD_hilb-F_bpass-F_comp-best_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30,20 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l2 --weight_reg_strength 0.72 --activation_fct elu --filetype SSD --hilbert_power False --band_pass False--component 3 --hrcomp True --path_specificities BiCl_RndHPS_lstm-30-20_fc-0_lr-1e-3_wreg-l2-0.72_actfunc-elu_ftype-SSD_hilb-F_bpass-F_comp-3_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 50 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l2 --weight_reg_strength 1.44 --activation_fct elu --filetype SSD --hilbert_power True --band_pass True--component 1,2,3,4 --hrcomp False --path_specificities BiCl_RndHPS_lstm-50_fc-0_lr-1e-2_wreg-l2-1.44_actfunc-elu_ftype-SSD_hilb-T_bpass-T_comp-1-2-3-4_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 50 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 0.18 --activation_fct elu --filetype SSD --hilbert_power False --band_pass False--component 1,2,3,4,5 --hrcomp False --path_specificities BiCl_RndHPS_lstm-50_fc-0_lr-1e-2_wreg-l1-0.18_actfunc-elu_ftype-SSD_hilb-F_bpass-F_comp-1-2-3-4-5_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 65,40 --fc_n_hidden 0 --learning_rate 5e-4 --weight_reg l2 --weight_reg_strength 0.72 --activation_fct elu --filetype SSD --hilbert_power True --band_pass False--component 1,2,3,4 --hrcomp False --path_specificities BiCl_RndHPS_lstm-65-40_fc-0_lr-5e-4_wreg-l2-0.72_actfunc-elu_ftype-SSD_hilb-T_bpass-F_comp-1-2-3-4_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 25,25 --fc_n_hidden 15 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.18 --activation_fct relu --filetype SSD --hilbert_power False --band_pass True--component 1,2,3,4,5 --hrcomp True --path_specificities BiCl_RndHPS_lstm-25-25_fc-15_lr-1e-3_wreg-l1-0.18_actfunc-relu_ftype-SSD_hilb-F_bpass-T_comp-1-2-3-4-5_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 25 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.18 --activation_fct elu --filetype SSD --hilbert_power False --band_pass True--component 1,2,3,4,5 --hrcomp False --path_specificities BiCl_RndHPS_lstm-25_fc-0_lr-1e-3_wreg-l1-0.18_actfunc-elu_ftype-SSD_hilb-F_bpass-T_comp-1-2-3-4-5_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 80,65 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct elu --filetype SSD --hilbert_power True --band_pass False--component 2,5,6,7 --hrcomp True --path_specificities BiCl_RndHPS_lstm-80-65_fc-0_lr-1e-3_wreg-l1-0.36_actfunc-elu_ftype-SSD_hilb-T_bpass-F_comp-2-5-6-7_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 10,10 --fc_n_hidden 10 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct elu --filetype SSD --hilbert_power False --band_pass True--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-10-10_fc-10_lr-1e-3_wreg-l1-0.36_actfunc-elu_ftype-SSD_hilb-F_bpass-T_comp-best_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30 --fc_n_hidden 0 --learning_rate 5e-4 --weight_reg l2 --weight_reg_strength 0.36 --activation_fct relu --filetype SSD --hilbert_power False --band_pass True--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-30_fc-0_lr-5e-4_wreg-l2-0.36_actfunc-relu_ftype-SSD_hilb-F_bpass-T_comp-best_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 80 --fc_n_hidden 0 --learning_rate 1e-1 --weight_reg l1 --weight_reg_strength 0.18 --activation_fct relu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp True --path_specificities BiCl_RndHPS_lstm-80_fc-0_lr-1e-1_wreg-l1-0.18_actfunc-relu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 25 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l2 --weight_reg_strength 0.36 --activation_fct elu --filetype SSD --hilbert_power True --band_pass True--component 1,2,3,4 --hrcomp True --path_specificities BiCl_RndHPS_lstm-25_fc-0_lr-1e-3_wreg-l2-0.36_actfunc-elu_ftype-SSD_hilb-T_bpass-T_comp-1-2-3-4_hrcomp-T/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30,20 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct relu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-30-20_fc-0_lr-1e-3_wreg-l1-0.36_actfunc-relu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 50,15 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l2 --weight_reg_strength 0.72 --activation_fct elu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-50-15_fc-0_lr-1e-2_wreg-l2-0.72_actfunc-elu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-F/
python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 80,20 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 1e-05 --activation_fct relu --filetype SSD --hilbert_power False --band_pass False--component 1,2,3,4,5 --hrcomp True --path_specificities BiCl_RndHPS_lstm-80-20_fc-0_lr-1e-3_wreg-l1-0.00_actfunc-relu_ftype-SSD_hilb-F_bpass-F_comp-1-2-3-4-5_hrcomp-T/