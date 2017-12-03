# coding=utf-8
"""
Plot predictions made by the LSTM model

Author: Simon Hofmann | <[surname].[lastname][at]protonmail.com> | 2017
"""

from Load_Data import *
from tensorflow import gfile
import string
if platform.system() != 'Darwin':
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
else:
    import matplotlib.pyplot as plt


# Save plot
@true_false_request
def save_request():
    print("Do you want to save the plots")


try:
    plots = sys.argv[1]
    try:
        int(plots)
        plots = save_request()
        script_external_exe = False
    except ValueError:
        plots = True if "True" in plots else False
        script_external_exe = True
except IndexError:
    plots = save_request()
    script_external_exe = True


if script_external_exe:
    subject = sys.argv[2]
else:
    subject = input("Enter subject number (int): ")
    assert float(subject).is_integer(), "subject number must be integer"
subject = int(subject)

if script_external_exe:
    try:
        path_specificity = sys.argv[3]
    except IndexError:
        path_specificity = ""  # this way path given via terminal, e.g., python3 LSTM_pred_plot.py False False lstm-150
else:
    path_specificity = input("Provide specific subfolder (if any), in form 'subfolder/': ")

assert path_specificity == "" or path_specificity[-1] == "/", "path_specificity must be either empty or end with '/'"

wdic = "./LSTM"
wdic_plot = "../../Results/Plots/LSTM/"
wdic_lists = wdic + "/logs"
lw = 0.5  # linewidth

wdic_sub = wdic + "/S{}/{}".format(str(subject).zfill(2), path_specificity)
wdic_lists_sub = wdic_lists + "/S{}/{}".format(str(subject).zfill(2), path_specificity)

# Find correct files (csv-tables)
shuff_filename = "None"
for file in os.listdir(wdic_sub):
    if ".csv" in file:
        if "val_" in file:
            val_filename = file
        else:
            file_name = file

    elif ".txt" in file:
        acc_filename = file

    elif ".npy" in file:
        shuff_filename = file

# Intermediate step: check whether filenames alreay exist in already_plotted_dic
if plots:
    already_plotted_dic = wdic + "/S{}/already_plotted/".format(str(subject).zfill(2))
    if not gfile.Exists(already_plotted_dic):
        gfile.MakeDirs(already_plotted_dic)

    # add subfix if filename already exists
    abc = ''
    abc_counter = 0
    new_file_name = acc_filename  # could be also 'file_name' or 'val_filename'
    while os.path.exists(already_plotted_dic + new_file_name):
        new_file_name = new_file_name.split(abc + "_S")[0] + string.ascii_lowercase[abc_counter] \
                        + "_S" + new_file_name.split("_S")[1]
        abc = string.ascii_lowercase[abc_counter]
        abc_counter += 1

# Load data
pred_matrix = np.loadtxt(wdic_sub + file_name, delimiter=",")
val_pred_matrix = np.loadtxt(wdic_sub + val_filename, delimiter=",")

# Look for shuffle matrix
if os.path.exists(wdic_sub + shuff_filename):
    shuffle_order_matrix = np.load(wdic_sub + shuff_filename)

    # shuffle_order_fold5 = np.load(wdic_lists + "/S22/test_task-class_shuffle-T/5/5_shuffle_order.npy")
    dub_shuffle_order_matrix = np.repeat(a=shuffle_order_matrix, repeats=2, axis=0)

    # Correct oder of matrices according to shuffle order of each fold (saved in shuffle_order_matrix)
    pred_matrix = sort_mat_by_mat(mat=pred_matrix, mat_idx=dub_shuffle_order_matrix)

    val_pred_matrix = sort_mat_by_mat(mat=val_pred_matrix, mat_idx=dub_shuffle_order_matrix)
    del dub_shuffle_order_matrix

# Number of Folds
s_fold = int(len(pred_matrix[:, 0])/2)

# Import accuracies
acc_date = np.loadtxt(wdic_sub + acc_filename, dtype=str, delimiter=";")  # Check (before ",")
task = "regession"  # default
for info in acc_date:

    if "Task:" in info:
        task = info.split(": ")[1]

    elif "Shuffle_data:" in info:
        shuffle = True if info.split(": ")[1] == "True" else False
        if shuffle:
            assert os.path.exists(wdic_sub + shuff_filename), "shuffle_order_matrix is missing"

    elif "Hilbert_z-Power:" in info:
        hilb = info.split(": ")[1]
        hilb = True if "True" in hilb else False

    elif "repetition_set:" in info:
        reps = float(info.split(": ")[1])

    elif "batch_size:" in info:
        batch_size = int(info.split(": ")[1])

    elif "batch_random:" in info:
        rnd_batch = info.split(": ")[1]
        rnd_batch = True if rnd_batch in "True" else False

    elif "S-Fold(Round):" in info:
        s_rounds = np.array(list(map(int, info.split(": [")[1][0:-1].split(" "))))

    elif "Validation-Acc:" in info:
        val_acc = info.split(": ")[1].split(", ")  # Check (before "  ")
        v = []
        for i, item in enumerate(val_acc):
            if i == 0:  # first
                v.append(float(item[1:]))
            elif i == (len(val_acc)-1):  # last one
                v.append(float(item[0:-1]))
            else:
                v.append(float(item))
        val_acc = v
        del v

    elif "mean(Accuracy):" in info:
        mean_acc = np.round(a=float(info.split(": ")[1]), decimals=3)

    elif "zero_line_acc:" in info:
        zero_line_acc = float(info.split(": ")[1])

    elif "Validation-Class-Acc:" in info:
        val_class_acc = info.split(": ")[1].split(", ")  # Check (before "  ")
        v = []
        for i, item in enumerate(val_class_acc):
            if i == 0:  # first
                v.append(float(item[1:]))
            elif i == (len(val_class_acc) - 1):  # last one
                v.append(float(item[0:-1]))
            else:
                v.append(float(item))
        val_class_acc = v
        del v

    # elif "mean(Classification_Accuracy):" in info:
    #     mean_class_acc = np.round(a=float(info.split(": ")[1]), decimals=3)

# Load full rating vector
# whole_rating = np.nanmean(a=np.delete(arr=pred_matrix, obj=np.arange(0, 2*s_fold-1, 2), axis=0), axis=0)
whole_rating = load_rating_files(subjects=subject, bins=True)[str(subject)]["SBA"]["NoMov"]
whole_rating[np.where(whole_rating == 0)] = np.nan
if task == "classification":
    real_rating = normalization(array=load_rating_files(subjects=subject, bins=False)[str(subject)]["SBA"]["NoMov"],
                                lower_bound=-1, upper_bound=1)  # range [-1, 1]

    tertile = int(len(real_rating)/3)
    lower_tert_bound = np.sort(real_rating)[tertile]    # np.percentile(a=real_rating, q=33.33)
    upper_tert_bound = np.sort(real_rating)[tertile*2]  # np.percentile(a=real_rating, q=66.66)

    no_entries = np.isnan(np.nanmean(a=np.vstack((pred_matrix, val_pred_matrix)), axis=0))
    only_entries_rating = copy.copy(real_rating)
    only_entries_rating[np.where(no_entries)] = np.nan

# Exchange mean_acc, if:
if task == "classification":
    mean_acc = np.round(np.mean(calc_binary_class_accuracy(prediction_matrix=val_pred_matrix)), 3)
    # == np.round(np.nanmean(val_class_acc), 3)


# Subplot division
def subplot_div(n_s_fold):
    if n_s_fold < 10:
        sub_rows_f, sub_col_f, sub_n_f = n_s_fold, 1, 0
    else:
        sub_rows_f, sub_col_f, sub_n_f = int(n_s_fold / 2), 2, 0

    return sub_rows_f, sub_col_f, sub_n_f


# # Plot predictions
# open frame
figsize = (12, s_fold * (3 if s_fold < 4 else 1))
fig = plt.figure("{}-Folds | S{} | {} | mean(val_acc)={} | 1Hz".format(s_fold, str(subject).zfill(2), task, mean_acc),
                 figsize=figsize)

# Prepare subplot division
sub_rows, sub_col, sub_n = subplot_div(n_s_fold=s_fold)

# For each fold create plot
for fold in range(s_fold):

    # Vars to plot
    pred = pred_matrix[fold*2, :]
    rating = pred_matrix[fold*2 + 1, :]
    val_pred = val_pred_matrix[fold*2, :]
    val_rating = val_pred_matrix[fold*2 + 1, :]

    # add subplot
    sub_n += 1
    fig.add_subplot(sub_rows, sub_col, sub_n)

    # plot
    # plt.plot(pred, label="prediction", marker='o', markersize=3)  # , style='r-'
    # plt.plot(rating, ls="dotted", label="rating", marker='o', mfc='none', markersize=3)
    # plt.plot(val_pred, label="val_prediction", marker='o', markersize=3)
    # plt.plot(val_rating, ls="dotted", label="val_rating", marker='o', mfc='none', markersize=3)
    if task == "regression":
        # Predictions
        plt.plot(pred, color="steelblue", linewidth=lw, label="train-pred")  # , style='r-'
        plt.plot(val_pred, color="xkcd:coral", linewidth=lw, label="val-pred")
        # Ratings
        plt.plot(whole_rating, ls="dotted", color="black", label="rating")
        fold_acc = np.round(val_acc[int(np.where(np.array(s_rounds) == fold)[0])], 3)
    else:  # == "classification"
        # Predictions
        plt.plot(pred, marker="o", markerfacecolor="None", ms=2, color="steelblue", linewidth=lw, label="train-pred")
        plt.plot(val_pred, marker="o", markerfacecolor="None", ms=2, color="xkcd:coral", linewidth=lw,
                 label="val-pred")
        # Ratings
        plt.plot(real_rating, color="darkgrey", alpha=.5)
        plt.plot(only_entries_rating, color="teal", alpha=.3, label="rating")
        plt.plot(whole_rating, ls="None", marker="s", markerfacecolor="None", ms=2, color="black",
                 label="arousal: low=-1 | high=1")
        # midline and tertile borders
        plt.hlines(y=0, xmin=0, xmax=pred_matrix.shape[1], colors="darkgrey", lw=lw, alpha=.8)
        plt.hlines(y=lower_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
                   alpha=.8)
        plt.hlines(y=upper_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
                   alpha=.8)
        # Correct classified
        corr_class_train = np.sign(pred * rating)
        corr_class_val = np.sign(val_pred * val_rating)
        for i in range(corr_class_train.shape[0]):
            corr_col_train = "green" if corr_class_train[i] == 1 else "red"
            corr_col_val = "lime" if corr_class_val[i] == 1 else "orangered"
            plt.vlines(i, ymin=whole_rating[i], ymax=pred[i], colors=corr_col_train, alpha=.5, lw=lw/1.5)
            if not np.isnan(pred[i]):
                # set a point at the end of line
                plt.plot(i, whole_rating[i], marker="o", color=corr_col_train, alpha=.5, ms=1)
            plt.vlines(i, ymin=whole_rating[i], ymax=val_pred[i], colors=corr_col_val, alpha=.5, lw=lw/1.5)
            if not np.isnan(val_pred[i]):
                plt.plot(i, whole_rating[i], marker="o", color=corr_col_val, alpha=.5, ms=1)
        corr_class_val = np.delete(corr_class_val, np.where(np.isnan(corr_class_val)))
        if len(corr_class_val) > 0:
            fold_acc = np.round(sum(corr_class_val[corr_class_val == 1])/len(corr_class_val), 3)
            # ==val_class_acc[fold]
        else:
            fold_acc = np.nan

    plot_acc = np.round(val_acc[int(np.where(np.array(s_rounds) == fold)[0])], 3)
    plt.title(s="{}-Fold | val-acc={}".format(fold+1, fold_acc))  # fold_acc
    if fold == 0:
        plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)

    # adjust size, add legend
    plt.xlim(0, len(pred))
    plt.ylim(-1.2, 2)

plt.xlabel("time(s)")
plt.tight_layout(pad=2)
fig.show()

if plots:
    plot_filename = "{}{}_|{}{}*{}({})_|_{}-Folds_|_{}_|_S{}_|_mean(val_acc)_{:.2f}_|_{}.png".format(
        file_name[0:10], abc, "_Hilbert_" if hilb else "_", int(reps),
        "rnd-batch" if rnd_batch else "subsequent-batch", batch_size, s_fold, task,
        str(subject).zfill(2), mean_acc,
        path_specificity[:-1])

    fig.savefig(wdic_plot + plot_filename)

# # Plot accuracy-trajectories
fig2 = plt.figure("{}-Folds Accuracies | S{} | {} | mean(val_acc)={} | 1Hz ".format(s_fold,
                                                                                    str(subject).zfill(2), task,
                                                                                    mean_acc), figsize=figsize)

# Prepare subplot division
sub_rows, sub_col, sub_n = subplot_div(n_s_fold=s_fold)

for fold in range(s_fold):

    # Load Data
    train_acc_fold = np.loadtxt(wdic_lists_sub + "{}/train_acc_list.txt".format(fold), delimiter=",")
    val_acc_fold = np.loadtxt(wdic_lists_sub + "{}/val_acc_list.txt".format(fold), delimiter=",")
    val_acc_training_fold = [eval(line.split("\n")[0])
                             for line in open(wdic_lists_sub + "{}/val_acc_training_list.txt".format(fold))]

    # Attach also last val_acc to list
    last_acc = (np.nanmean(val_acc_fold), len(train_acc_fold)-1)
    val_acc_training_fold.append(last_acc)

    vacc, where = zip(*val_acc_training_fold)

    # Save average for later plot
    if fold == 0:
        x_fold_mean_vacc = np.array(vacc)
        x_fold_mean_tacc = train_acc_fold
    else:
        x_fold_mean_vacc += np.array(vacc)
        x_fold_mean_tacc += train_acc_fold
        if fold == s_fold-1:  # when last fold added, divide by s_fold
            x_fold_mean_vacc /= s_fold
            x_fold_mean_tacc /= s_fold

    # add subplot
    sub_n += 1
    fig2.add_subplot(sub_rows, sub_col, sub_n)

    plt.plot(train_acc_fold, color="steelblue", linewidth=lw/2, alpha=0.6, label="training accuracy")
    plt.plot(where, vacc, color="xkcd:coral", linewidth=2*lw, alpha=0.9, label="validation accuracy")
    plt.hlines(y=zero_line_acc, xmin=0, xmax=train_acc_fold.shape[0], colors="red", linestyles="dashed", lw=2*lw)

    plt.title(s="{}-Fold | val-acc={}".format(fold + 1,
                                              np.round(val_acc[int(np.where(np.array(s_rounds) == fold)[0])], 3)))

    # adjust size, add legend
    plt.xlim(0, len(train_acc_fold))
    plt.ylim(0.0, 1.5)
    if fold == 0:
        plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
        plt.ylabel("accuracy")

plt.xlabel("Training iterations")
plt.tight_layout(pad=2)

fig2.show()

# Plot
if task == "regression":
    if plots:
        plot_filename = "{}{}_|{}{}*{}({})_|_{}-Folds_|_Accuracies_|_S{}_|_mean(val_acc)_{:.2f}_|_{}.png".format(
            file_name[0:10], abc, "_Hilbert_" if hilb else "_", int(reps),
            "rnd-batch" if rnd_batch else "subsequent-batch", batch_size, s_fold, str(subject).zfill(2), mean_acc,
            path_specificity[:-1])

        fig2.savefig(wdic_plot + plot_filename)

else:  # task == "classification"
    plt.close()


# # Plot loss-trajectories

fig3 = plt.figure("{}-Folds Loss | S{} | {} | mean(val_acc)={} | 1Hz ".format(s_fold, str(subject).zfill(2), task,
                                                                              mean_acc), figsize=figsize)

# Prepare subplot division
sub_rows, sub_col, sub_n = subplot_div(n_s_fold=s_fold)

for fold in range(s_fold):
    # Load Data
    val_loss_fold = np.loadtxt(wdic_lists_sub + "{}/val_loss_list.txt".format(fold), delimiter=",")
    train_loss_fold = np.loadtxt(wdic_lists_sub + "{}/train_loss_list.txt".format(fold), delimiter=",")
    val_loss_training_fold = [eval(line.split("\n")[0])
                              for line in open(wdic_lists_sub + "{}/val_loss_training_list.txt".format(fold))]

    # Attach also last val_loss to list
    last_loss = (np.nanmean(val_loss_fold), len(train_loss_fold) - 1)
    val_loss_training_fold.append(last_loss)

    vloss, where_loss = zip(*val_loss_training_fold)

    # Save average for later plot
    if fold == 0:
        x_fold_mean_vloss = np.array(vloss)
        x_fold_mean_tloss = train_loss_fold
    else:
        x_fold_mean_vloss += np.array(vloss)
        x_fold_mean_tloss += train_loss_fold
        if fold == s_fold - 1:  # when last fold added, divide by s_fold
            x_fold_mean_vloss /= s_fold
            x_fold_mean_tloss /= s_fold

    # add subplot
    sub_n += 1
    fig3.add_subplot(sub_rows, sub_col, sub_n)

    # plot
    plt.plot(train_loss_fold, color="steelblue", linewidth=lw/2, alpha=0.6, label="training loss")
    plt.plot(where_loss, vloss, color="xkcd:coral", linewidth=2*lw, alpha=0.9, label="validation loss")

    plt.title(s="{}-Fold | val-loss={}".format(fold + 1,
                                               np.round(val_acc[int(np.where(np.array(s_rounds) == fold)[0])], 3)))

    # adjust size, add legend
    plt.xlim(0, len(train_loss_fold))
    plt.ylim(-0.05, 1.8)
    if fold == 0:
        plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
        plt.ylabel("Loss")

plt.xlabel("Training iterations")
plt.tight_layout(pad=2)

fig3.show()

# Plot
if task == "regression":
    if plots:
        plot_filename = "{}{}_|{}{}*{}({})_|_{}-Folds_|_Loss_|_S{}_|_mean(val_acc)_{:.2f}_|_{}.png".format(
            file_name[0:10], abc, "_Hilbert_" if hilb else "_", int(reps),
            "rnd-batch" if rnd_batch else "subsequent-batch", batch_size, s_fold, str(subject).zfill(2), mean_acc,
            path_specificity[:-1])

        fig3.savefig(wdic_plot + plot_filename)
else:  # task == "classification"
    plt.close()

# # Plot i) average training prediction and ii) concatenated val_prediction

fig4 = plt.figure("{}-Folds mean(train)_&_concat(val)_| S{} | {} | mean(val_acc)={} | 1Hz ".format(
    s_fold, str(subject).zfill(2), task, mean_acc), figsize=(10, 12))

# delete ratings out of pred_matrix first and then average across rows
average_train_pred = np.nanmean(a=np.delete(arr=pred_matrix, obj=np.arange(1, 2*s_fold, 2), axis=0), axis=0)
concat_val_pred = np.nanmean(a=np.delete(arr=val_pred_matrix, obj=np.arange(1, 2*s_fold, 2), axis=0), axis=0)
# whole_rating = np.nanmean(a=np.delete(arr=pred_matrix, obj=np.arange(0, 2*s_fold-1, 2), axis=0), axis=0)

# Plot average train prediction
fig4.add_subplot(4, 1, 1)
if task == "regression":
    # Predictions
    plt.plot(average_train_pred, color="steelblue", linewidth=2*lw, label="mean train-prediction")  # , style='r-'
    # Ratings
    plt.plot(whole_rating, ls="dotted", color="black", label="rating")
    plt.title(s="Average train prediction | {}-Folds".format(s_fold))
else:  # if task == "classification":
    # Predictions
    plt.plot(average_train_pred, color="steelblue", marker="o", markerfacecolor="None", ms=2, linewidth=2*lw,
             label="mean_train_prediction")
    # Ratings
    plt.plot(real_rating, color="darkgrey", alpha=.5)
    plt.plot(only_entries_rating, color="teal", alpha=.3, label="ground-truth rating")
    plt.plot(whole_rating, ls="None", marker="s", markerfacecolor="None", ms=3, color="black",
             label="arousal classes: low=-1 | high=1")
    # midline and tertile borders
    plt.hlines(y=0, xmin=0, xmax=pred_matrix.shape[1], colors="darkgrey", lw=lw, alpha=.8)
    plt.hlines(y=lower_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
               alpha=.8)
    plt.hlines(y=upper_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
               alpha=.8)
    # Correct classified
    correct_class_train = np.sign(average_train_pred * whole_rating)
    for i in range(correct_class_train.shape[0]):
        corr_col = "green" if correct_class_train[i] == 1 else "red"
        plt.vlines(i, ymin=whole_rating[i], ymax=average_train_pred[i], colors=corr_col, alpha=.5, lw=lw/1.5)
        if not np.isnan(average_train_pred[i]):
            # set a point at the end of line
            plt.plot(i, whole_rating[i], marker="o", color=corr_col, alpha=.5, ms=2)
    correct_class_train = np.delete(correct_class_train, np.where(np.isnan(correct_class_train)))
    mean_train_acc = sum(correct_class_train[correct_class_train == 1])/len(correct_class_train)
    plt.xlabel("time(s)")
    plt.title(s="Average train prediction | {}-Folds| {} | mean_train_class_acc={:.3f}".format(s_fold,
                                                                                               task,
                                                                                               mean_train_acc))

# adjust size, add legend
plt.xlim(0, len(whole_rating))
plt.ylim(-1.2, 2)
plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
plt.tight_layout(pad=2)

# Plot average train prediction
fig4.add_subplot(4, 1, 2)
if task == "regression":
    plt.plot(concat_val_pred, c="xkcd:coral", linewidth=2*lw, label="concatenated val-prediction")
    plt.plot(whole_rating, ls="dotted", color="black", label="rating")
else:  # task == "classification":

    plt.plot(concat_val_pred, marker="o", markerfacecolor="None", ms=2, c="xkcd:coral", linewidth=2*lw,
             label="concatenated val-prediction")
    # Ratings
    plt.plot(real_rating, color="darkgrey", alpha=.5)
    plt.plot(only_entries_rating, color="teal", alpha=.3, label="ground-truth rating")
    plt.plot(whole_rating, ls="None", marker="s", markerfacecolor="None", ms=3, color="black",
             label="arousal classes: low=-1 | high=1")
    # midline and tertile borders
    plt.hlines(y=0, xmin=0, xmax=pred_matrix.shape[1], colors="darkgrey", lw=lw, alpha=.8)
    plt.hlines(y=lower_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
               alpha=.8)
    plt.hlines(y=upper_tert_bound, xmin=0, xmax=pred_matrix.shape[1], linestyle="dashed", colors="darkgrey", lw=lw,
               alpha=.8)
    # Correct classified
    correct_class = np.sign(concat_val_pred * whole_rating)
    for i in range(correct_class.shape[0]):
        corr_col = "lime" if correct_class[i] == 1 else "orangered"
        plt.vlines(i, ymin=whole_rating[i], ymax=concat_val_pred[i], colors=corr_col, alpha=.5, lw=lw/1.5)
        if not np.isnan(concat_val_pred[i]):
            # set a point at the end of line
            plt.plot(i, whole_rating[i], marker="o", color=corr_col, alpha=.5, ms=2)
        # plt.vlines(i, ymin=concat_val_pred[i], ymax=whole_rating[i], colors=corr_col, alpha=.5, lw=lw)
        # print(whole_rating[i], concat_val_pred[i])

plt.xlabel("time(s)")
plt.title(s="Concatenated val-prediction | {}-Folds | {} | mean_val_acc={}".format(s_fold, task, np.round(mean_acc, 3)))
# adjust size, add legend
plt.xlim(0, len(whole_rating))
plt.ylim(-1.2, 2)
plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
plt.tight_layout(pad=2)

# # Plot i) average training & validation accuracy and ii) loss across folds

# Plot average training & validation accuracy
fig4.add_subplot(4, 1, 3)

plt.plot(x_fold_mean_tacc, color="steelblue", linewidth=lw/2, alpha=0.6, label="mean training accuracy")
plt.plot(where, x_fold_mean_vacc, color="xkcd:coral", linewidth=2*lw, alpha=0.9, label="mean validation accuracy")
if task == "regression":
    plt.hlines(y=zero_line_acc, xmin=0, xmax=train_acc_fold.shape[0], colors="red", linestyles="dashed", lw=2*lw)
else:  # == "classification"
    plt.hlines(y=.5, xmin=0, xmax=train_acc_fold.shape[0], colors="red", linestyles="dashed", lw=lw)
plt.xlabel("Training iterations")
plt.ylabel("Accuracy")
plt.title(s="Across all S-folds | mean training & validation accuracy")

# adjust size, add legend
plt.xlim(0, len(train_acc_fold))
plt.ylim(0.0, 1.5)
plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
plt.tight_layout(pad=2)

# Plot average training & validation loss
fig4.add_subplot(4, 1, 4)

plt.plot(x_fold_mean_tloss, color="steelblue", linewidth=lw/2, alpha=0.6,
         label="mean training loss")
plt.plot(where_loss, x_fold_mean_vloss, color="xkcd:coral", linewidth=2*lw, alpha=0.9,
         label="mean validation loss")
plt.xlabel("Training iterations")
plt.ylabel("Loss")
plt.title(s="Across all S-folds | mean training & validation loss")

# adjust size, add legend
plt.xlim(0, len(train_loss_fold))
plt.ylim(-0.05, 1.8)
plt.legend(bbox_to_anchor=(0., 0.90, 1., .102), loc=1, ncol=4, mode="expand", borderaxespad=0.)
plt.tight_layout(pad=2)

fig4.show()

# Plot
if plots:
    plot_filename = "{}{}_|{}{}*{}({})_|_{}-Folds_|_{}_|_all_train_val_|_S{}_|_mean(val_acc)_{:.2f}_|_{}.png".format(
        file_name[0:10], abc, "_Hilbert_" if hilb else "_", int(reps),
        "rnd-batch" if rnd_batch else "subsequent-batch", batch_size, s_fold, task, str(subject).zfill(2), mean_acc,
        path_specificity[:-1])

    fig4.savefig(wdic_plot + plot_filename)


@true_false_request
def close_plots():
    print("Do you want to close plots?")


if not script_external_exe:  # Check whether script is opened from intern(python) or extern(terminal)
    if close_plots():
        for _ in range(4):
            plt.close()

# When saved then move *.csv & *.txt files into folder "Already Plotted"
if plots:
    for file in os.listdir(wdic_sub):
        if file != 'already_plotted':
            new_file_name = file.split("_S")[0] + abc + "_S" + file.split("_S")[1]

            while True:
                try:
                    gfile.Rename(oldname=wdic_sub+file, newname=already_plotted_dic+new_file_name, overwrite=False)
                    break
                except Exception:
                    new_file_name = new_file_name.split(abc + "_S")[0] + string.ascii_lowercase[abc_counter] \
                                    + "_S" + new_file_name.split("_S")[1]
                    abc = string.ascii_lowercase[abc_counter]
                    abc_counter += 1

    # open folder
    open_folder(wdic_plot)