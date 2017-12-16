#!/usr/bin/env bash

# Random Search Bashfile_3: classification
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 15,10 --fc_n_hidden 0 --learning_rate 1e-1 --weight_reg l1 --weight_reg_strength 0.18 --activation_fct relu --filetype SPOC --hilbert_power True --band_pass True--component 1 --hrcomp True --path_specificities BiCl_RndHPS_lstm-15-10_fc-0_lr-1e-1_wreg-l1-0.18_actfunc-relu_ftype-SPOC_hilb-T_bpass-T_comp-1_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 15,10 --fc_n_hidden 10 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 0.72 --activation_fct relu --filetype SSD --hilbert_power False --band_pass False--component 5,6 --hrcomp True --path_specificities BiCl_RndHPS_lstm-15-10_fc-10_lr-1e-2_wreg-l1-0.72_actfunc-relu_ftype-SSD_hilb-F_bpass-F_comp-5-6_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l2 --weight_reg_strength 0.72 --activation_fct relu --filetype SSD --hilbert_power True --band_pass True--component 1,2,3,4,5 --hrcomp True --path_specificities BiCl_RndHPS_lstm-30_fc-0_lr-1e-3_wreg-l2-0.72_actfunc-relu_ftype-SSD_hilb-T_bpass-T_comp-1-2-3-4-5_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 30,15 --fc_n_hidden 10 --learning_rate 1e-2 --weight_reg l1 --weight_reg_strength 1.44 --activation_fct relu --filetype SSD --hilbert_power False --band_pass False--component 1,2,3,4,5 --hrcomp False --path_specificities BiCl_RndHPS_lstm-30-15_fc-10_lr-1e-2_wreg-l1-1.44_actfunc-relu_ftype-SSD_hilb-F_bpass-F_comp-1-2-3-4-5_hrcomp-F/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 15 --fc_n_hidden 0 --learning_rate 1e-3 --weight_reg l1 --weight_reg_strength 0.36 --activation_fct elu --filetype SPOC --hilbert_power False --band_pass True--component 1,2,3,4,5,6,7 --hrcomp True --path_specificities BiCl_RndHPS_lstm-15_fc-0_lr-1e-3_wreg-l1-0.36_actfunc-elu_ftype-SPOC_hilb-F_bpass-T_comp-1-2-3-4-5-6-7_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 20 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l2 --weight_reg_strength 0.36 --activation_fct relu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp False --path_specificities BiCl_RndHPS_lstm-20_fc-0_lr-1e-2_wreg-l2-0.36_actfunc-relu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-F/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 65 --fc_n_hidden 0 --learning_rate 5e-4 --weight_reg l2 --weight_reg_strength 1.44 --activation_fct relu --filetype SPOC --hilbert_power False --band_pass True--component 1,2,3,4,5,6,7 --hrcomp True --path_specificities BiCl_RndHPS_lstm-65_fc-0_lr-5e-4_wreg-l2-1.44_actfunc-relu_ftype-SPOC_hilb-F_bpass-T_comp-1-2-3-4-5-6-7_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 50,50 --fc_n_hidden 0 --learning_rate 1e-2 --weight_reg l2 --weight_reg_strength 0.36 --activation_fct elu --filetype SPOC --hilbert_power True --band_pass True--component 1,2 --hrcomp True --path_specificities BiCl_RndHPS_lstm-50-50_fc-0_lr-1e-2_wreg-l2-0.36_actfunc-elu_ftype-SPOC_hilb-T_bpass-T_comp-1-2_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 100 --fc_n_hidden 0 --learning_rate 1e-1 --weight_reg l1 --weight_reg_strength 1.44 --activation_fct elu --filetype SSD --hilbert_power False --band_pass True--component 1,2,3,4,5 --hrcomp True --path_specificities BiCl_RndHPS_lstm-100_fc-0_lr-1e-1_wreg-l1-1.44_actfunc-elu_ftype-SSD_hilb-F_bpass-T_comp-1-2-3-4-5_hrcomp-T/
# python3 NeVRo.py --subject 36 --seed True --task classification --shuffle True --repet_scalar 30 --s_fold 10 --batch_size 9 --successive 1 --successive_mode 1 --rand_batch True --plot True --lstm_size 15,10 --fc_n_hidden 0 --learning_rate 1e-1 --weight_reg l2 --weight_reg_strength 0.00001 --activation_fct elu --filetype SSD --hilbert_power True --band_pass False--component best --hrcomp True --path_specificities BiCl_RndHPS_lstm-15-10_fc-0_lr-1e-1_wreg-l2-0.00_actfunc-elu_ftype-SSD_hilb-T_bpass-F_comp-best_hrcomp-T/