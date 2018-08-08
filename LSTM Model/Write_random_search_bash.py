# coding=utf-8
"""
Write a random search bash file.

Author: Simon Hofmann | <[surname].[lastname][at]protonmail.com> | 2017
"""

import numpy as np
import os.path

n_sub = 45
all_subjects = np.linspace(start=1, stop=n_sub, num=n_sub, dtype=int)  # np.arange(1, n_sub+1)
dropouts = np.array([1, 12, 32, 33, 38, 40, 45])
# subjects = [2, 36]  # Done
# subjects = [22, 44]  # Done
# subjects = [28, 5, 6, 14, 17, 9]  # Done
subjects = np.setdiff1d(all_subjects, dropouts)  # these are all subjects without dropouts
subjects = np.setdiff1d(subjects, [2, 36]+[22, 44]+[28, 5, 6, 14, 17, 9])  # without already computed subjects
del_log_folders = True


def write_search_bash_files(subs):

    # Request
    n_combinations = int(input("How many combinations to test (given value will be multpied with n_subjects)): "))
    assert n_combinations % 4 == 0, "Number of combinations must be a multiple of 4"

    seed = True
    tasks = ["regression", "classification"]
    task_request = input("For which task is the random search bash? ['r' for'regression', 'c' for 'classification']: ")
    assert task_request.lower() in tasks[0] or task_request.lower() in tasks[1], "Input must be eitehr 'r' or 'c'"
    task = tasks[0] if task_request.lower() in tasks[0] else tasks[1]
    shuffle = True if task == "classification" else False
    repet_scalar = 30
    s_fold = 10
    batch_size = 9
    successive = 1 if task == "classification" else 3
    successive_mode = 1
    rand_batch = True
    plot = True

    # Create bashfile if not there already:
    bash_file_name = "bashfile_randomsearch_{}.sh".format('BiCl' if "c" in task else "Reg")
    if not os.path.exists(bash_file_name):
        with open(bash_file_name, "w") as bashfile:  # 'a' for append
            bashfile.write("#!/usr/bin/env bash\n\n" + "# Random Search Bashfile: {}".format(task))

        for sub_bash in ["_local.sh", "_1.sh", "_2.sh", "_3.sh"]:
            sub_bash_file_name = bash_file_name.split(".")[0] + sub_bash
            with open(sub_bash_file_name, "w") as bashfile:  # 'a' for append
                bashfile.write("#!/usr/bin/env bash\n\n"+"# Random Search Bashfile{}: {}".format(sub_bash.split(".")[0],
                                                                                                 task))

    # # Randomly Draw
    combi_count = 0
    for combi in range(n_combinations):

        # lstm_size
        n_lstm_layers = np.random.choice([1, 2])  # either 1 or 2 layers
        layer_size = [10, 15, 20, 25, 30, 40, 50, 65, 80, 100]  # possible layer sizes

        if n_lstm_layers == 1:
            lstm_size = np.random.choice(layer_size)
        else:  # n_lstm_layers == 2
            lstm_l1 = np.random.choice(layer_size)
            while True:  # size of second layer should be smaller or equal to size of first layer
                lstm_l2 = np.random.choice(layer_size)
                if lstm_l2 <= lstm_l1:
                    break
            lstm_size = "{},{}".format(lstm_l1, lstm_l2)

        # fc_n_hidden
        n_fc_layers = np.random.choice(range(n_lstm_layers))  # n_fc_layers <= n_lstm_layers
        # note: if n_fc_layers == len(fc_n_hidden) == 0, there is 1 fc-lay attached to lstm,
        # so 1 n_fc_layers == 2 fc layers

        if n_fc_layers == 0:
            fc_n_hidden = 0
        else:
            while True:
                fc_n_hidden = np.random.choice(layer_size)
                if n_lstm_layers == 1:
                    if fc_n_hidden <= lstm_size:
                        break
                else:  # n_lstm_layers == 2
                    if fc_n_hidden <= int(lstm_size.split(",")[1]):
                        break

        # learning_rate
        # learning_rate = np.random.choice(a=['1e-1', '1e-2', '1e-3', '5e-4'])
        learning_rate = np.random.choice(a=['1e-2', '1e-3', '5e-4'])

        # weight_reg
        weight_reg = np.random.choice(a=['l1', 'l2'])

        # weight_reg_strength
        weight_reg_strength = np.random.choice(a=[0.00001, 0.18, 0.36, 0.72, 1.44])  # 0. == no regularization

        # activation_fct
        activation_fct = np.random.choice(a=['elu', 'relu'])

        # filetype
        # filetype = np.random.choice(a=['SSD', 'SPOC'])
        filetype = 'SSD'

        # hilbert_power
        hilbert_power = np.random.choice(a=[True, False])

        # band_pass
        if filetype == "SPOC":
            band_pass = True  # there is no non-band-pass SPOC data (yet).
        else:  # filetype == "SSD"
            band_pass = np.random.choice(a=[True, False])

        # hrcomp
        hrcomp = np.random.choice(a=[True, False])

        # component
        component_modes = np.random.choice(a=["best", "random_set", "one_up"])

        # From here on it is subject-dependent
        max_n_comp = 99
        for subject in subs:
            if component_modes == "best":
                if filetype == "SPOC":
                    component = '1'  # SPOC orders comps w.r.t. correlation to target variable, hence 'best' is 1st comp
                else:
                    component = "best"

            else:  # component_modes == 'random_set' or == 'one_up'
                if filetype == "SSD":
                    wdic = "../../Data/EEG_SSD/SBA/Components/{}NoMov/".format("" if band_pass
                                                                               else "not_alpha_band_passed/")
                    filename = wdic + "NVR_S{}_SBA_NoMov_SSD_Components_SBA_CNT.txt".format(str(subject).zfill(2))

                else:  # filetype == "SPOC"
                    wdic = "../../Data/EEG_SPOC/SBA/Components/NoMov/"
                    filename = wdic + "NVR_S{}_SBA_NoMov_PREP_SPOC_Components.txt".format(str(subject).zfill(2))

                max_n_comp = max_n_comp if max_n_comp < len(np.genfromtxt(filename)[0]) \
                    else len(np.genfromtxt(filename)[0])

                # Randomly choice number of feed-components
                while True:
                    choose_n_comp = np.random.randint(1, max_n_comp+1)  # x
                    if choose_n_comp <= 10:  # don't feed more than 10 components
                        break

                if component_modes == "one_up":
                    # Choose from component 1 to n_choose (see: SPOC(comp_order), and SSD(alpha-hypotheses)):
                    component = np.arange(start=1, stop=choose_n_comp+1)  # range [1, n_choose]

                else:  # component_modes == "random_set"
                    # Choose x random components, where x == choose_n_comp
                    component = np.sort(np.random.choice(a=range(1, max_n_comp+1), size=choose_n_comp, replace=False))

                component = ','.join([str(i) for i in component])

        # path_specificities
        path_specificities = "{}RndHPS_lstm-{}_fc-{}_lr-{}_wreg-{}-{:.2f}_actfunc-{}_ftype-{}_hilb-{}_bpass-{}" \
                             "_comp-{}_hrcomp-{}/".format('BiCl_' if "c" in task else "Reg_",
                                                          "-".join(str(lstm_size).split(",")), "-".join(
                                                            str(fc_n_hidden).split(",")),
                                                          learning_rate, weight_reg, weight_reg_strength,
                                                          activation_fct, filetype,
                                                          "T" if hilbert_power else "F", "T" if band_pass else "F",
                                                          "-".join(str(component).split(",")), "T" if hrcomp else "F")

        # Write line for bashfile
        for subject in subs:
            bash_line = "python3 NeVRo.py " \
                        "--subject {} --seed {} --task {} --shuffle {} " \
                        "--repet_scalar {} --s_fold {} --batch_size {} " \
                        "--successive {} --successive_mode {} --rand_batch {} " \
                        "--plot {} --dellog {} " \
                        "--lstm_size {} --fc_n_hidden {} --learning_rate {} " \
                        "--weight_reg {} --weight_reg_strength {} " \
                        "--activation_fct {} " \
                        "--filetype {} --hilbert_power {} --band_pass {} " \
                        "--component {} --hrcomp {} " \
                        "--path_specificities {}".format(subject, seed, task, shuffle,
                                                         repet_scalar, s_fold, batch_size,
                                                         successive, successive_mode, rand_batch,
                                                         plot, del_log_folders,
                                                         lstm_size, fc_n_hidden, learning_rate,
                                                         weight_reg, weight_reg_strength,
                                                         activation_fct,
                                                         filetype, hilbert_power, band_pass,
                                                         component, hrcomp,
                                                         path_specificities)

            # Write in bashfile
            with open(bash_file_name, "a") as bashfile:  # 'a' for append
                bashfile.write("\n"+bash_line)

            # and in subbashfile
            sub_bash = ["_local.sh", "_1.sh", "_2.sh", "_3.sh"][combi_count]
            sub_bash_file_name = bash_file_name.split(".")[0] + sub_bash
            with open(sub_bash_file_name, "a") as sub_bashfile:  # 'a' for append
                sub_bashfile.write("\n"+bash_line)

            # Fill in Random_Search_Table.csv
            table_name = "./LSTM/Random_Search_Table_{}.csv".format('BiCl' if "c" in task else "Reg")

            if not os.path.exists(table_name):
                rs_table = np.array(['round', 'subject', 'seed', 'task', 'shuffle', 'repet_scalar',
                                     's_fold', 'batch_size', 'successive', 'successive_mode',
                                     'rand_batch', 'plot', 'lstm_size', 'fc_n_hidden', 'learning_rate',
                                     'weight_reg', 'weight_reg_strength', 'activation_fct', 'filetype',
                                     'hilbert_power', 'band_pass', 'component', 'hrcomp',
                                     'path_specificities', 'mean_val_acc', 'zeroline_acc',
                                     'mean_class_val_acc'], dtype='<U113')  # Could write del_log_folders in table
            else:
                rs_table = np.genfromtxt(table_name, delimiter=";", dtype=str)

            rs_table = np.reshape(rs_table, newshape=(-1, 27))

            rnd = int(rs_table[-1, 0]) + 1 if rs_table[-1, 0].isnumeric() else 0

            exp_data = [rnd, subject, seed, task,
                        shuffle, repet_scalar, s_fold, batch_size, successive, successive_mode,
                        rand_batch, plot, lstm_size, fc_n_hidden, learning_rate, weight_reg, weight_reg_strength,
                        activation_fct, filetype, hilbert_power, band_pass, component, hrcomp, path_specificities]

            fill_vec = np.repeat(a="nan", repeats=rs_table.shape[1])
            fill_vec = fill_vec.reshape((-1, len(fill_vec)))
            rs_table = np.concatenate((rs_table, fill_vec), axis=0).astype("<U120")
            rs_table[-1, 0:len(exp_data)] = exp_data

            np.savetxt(fname=table_name, X=rs_table, delimiter=";", fmt="%s")

            # Set Counter
            combi_count = combi_count+1 if combi_count < 3 else 0

    print("\nBashfiles and Table completed.")

# write_search_bash_files(subs=subjects)


def write_bash_from_table(subs, table_path):

    wd_tables = "./LSTM/Random Search Tables/"
    table_path = wd_tables + table_path
    # table_path = wd_tables + "unique_Best_2_HPsets_over_10_Subjects_mean_acc_0.660_Random_Search_Table_BiCl.csv"

    if not isinstance(subs, list) and not isinstance(subs, np.ndarray):
        subs = [subs]

    num_sub = len(subs)

    assert os.path.exists(table_path), "Given table path does not exist"
    hp_table = np.genfromtxt(table_path, delimiter=";", dtype=str)

    # Create new HP-table
    n_combis = hp_table[1:].shape[0]
    rounds = np.arange(n_combis*num_sub)
    rounds = np.reshape(rounds, newshape=(len(rounds), 1))
    subs = np.tile(subs, n_combis)
    subs = np.reshape(subs, newshape=(len(subs), 1))
    lside_table = np.concatenate((rounds, subs), 1)
    lside_header = np.reshape(np.array(['round', 'subject'], dtype='<U113'), newshape=(1, 2))
    lside_table = np.concatenate((lside_header, lside_table))
    rside_header = np.reshape(np.array(['mean_val_acc', 'zeroline_acc', 'mean_class_val_acc'], dtype='<U113'), (1, 3))
    rside_table = np.reshape(np.repeat(np.repeat(a="nan", repeats=n_combis*num_sub), 3), newshape=(-1, 3))
    rside_table = np.concatenate((rside_header, rside_table))
    mid_table = np.repeat(hp_table[1:, :], num_sub, axis=0)
    mid_header = np.reshape(hp_table[0, :], newshape=(1, -1))
    mid_table = np.concatenate((mid_header, mid_table))

    new_hp_table = np.concatenate((np.concatenate((lside_table, mid_table), 1), rside_table), 1)

    # Save new HP-table
    new_table_name = "./LSTM/" + "Ran" + table_path.split("_Ran")[-1]
    np.savetxt(fname=new_table_name, X=new_hp_table, delimiter=";", fmt="%s")

    # Create bashfile if not there already:
    bash_filename = "bashfile_specific_search_{}.sh".format(table_path.split("_")[-1].split(".")[0])
    if not os.path.exists(bash_filename):
        with open(bash_filename, "w") as bash_file:  # 'a' for append
            bash_file.write("#!/usr/bin/env bash\n\n" + "# Specific Search Bashfile:")

        for subbash in ["_local.sh", "_1.sh", "_2.sh", "_3.sh"]:
            subbash_filename = bash_filename.split(".")[0] + subbash
            with open(subbash_filename, "w") as bash_file:  # 'a' for append
                bash_file.write(
                    "#!/usr/bin/env bash\n\n" + "# Specific Search Bashfile{}:".format(subbash.split(".")[0]))

    # Write according bashfiles
    combi_count = 0
    for line in new_hp_table[1:, 1:-3]:

        subject, seed, task, shuffle, \
            repet_scalar, s_fold, batch_size,\
            successive, successive_mode, rand_batch, \
            plot, \
            lstm_size, fc_n_hidden, learning_rate, \
            weight_reg, weight_reg_strength,\
            activation_fct, \
            filetype, hilbert_power, band_pass, \
            component, hrcomp, \
            path_specificities = line

        # Write line for bashfile (Important: [Space] after each entry)

        bash_line = "python3 NeVRo.py " \
                    "--subject {} --seed {} --task {} --shuffle {} " \
                    "--repet_scalar {} --s_fold {} --batch_size {} " \
                    "--successive {} --successive_mode {} --rand_batch {} " \
                    "--plot {} --dellog {} " \
                    "--lstm_size {} --fc_n_hidden {} --learning_rate {} " \
                    "--weight_reg {} --weight_reg_strength {} " \
                    "--activation_fct {} " \
                    "--filetype {} --hilbert_power {} --band_pass {} " \
                    "--component {} --hrcomp {} " \
                    "--path_specificities {}".format(subject, seed, task, shuffle,
                                                     repet_scalar, s_fold, batch_size,
                                                     successive, successive_mode, rand_batch,
                                                     plot, del_log_folders,
                                                     lstm_size, fc_n_hidden, learning_rate,
                                                     weight_reg, weight_reg_strength,
                                                     activation_fct,
                                                     filetype, hilbert_power, band_pass,
                                                     component, hrcomp,
                                                     path_specificities)

        # Write in bashfile
        with open(bash_filename, "a") as bashfile:  # 'a' for append
            bashfile.write("\n" + bash_line)

        # and in subbashfile
        subbash = ["_local.sh", "_1.sh", "_2.sh", "_3.sh"][combi_count]
        sub_bash_file_name = bash_filename.split(".")[0] + subbash
        with open(sub_bash_file_name, "a") as subbashfile:  # 'a' for append
            subbashfile.write("\n" + bash_line)

        # Set Counter
        combi_count = combi_count + 1 if combi_count < 3 else 0

    print("\nBashfiles and Table completed.")
# write_bash_from_table(subs=subjects,
#                       table_path='unique_Best_2_HPsets_over_10_Subjects_mean_acc_0.660_Random_Search_Table_BiCl.csv')
# write_bash_from_table(subs=subjects,
#                       table_path='unique_Best_2_HPsets_over_10_Subjects_mean_acc_0.046_Random_Search_Table_Reg.csv')