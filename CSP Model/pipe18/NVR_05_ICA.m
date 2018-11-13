%% NVR_EventsAro
%This script adds the arousal events to the NeVRo EEG data. 

function NVR_05_ICA(cropstyle, mov_cond, varargin) 

%% 1.Set Variables
%clc
%clear all

if nargin>2
    icatype = varargin{1};
else
    icatype = 'runica';
end

%1.1 Set different paths:
path_data = '../../Data/';
path_dataeeg =  [path_data 'EEG/'];
path_in_eeg = [path_dataeeg 'eventsAro/' mov_cond '/' cropstyle '/']; 

% output paths:
path_out_eeg = [path_dataeeg 'cleanICA/' mov_cond '/' cropstyle '/'];
if ~exist(path_out_eeg, 'dir'); mkdir(path_out_eeg); end
path_reports = [path_out_eeg 'reports/'];
if ~exist(path_reports, 'dir'); mkdir(path_reports); end

%1.2 Get data files
files_eeg = dir([path_in_eeg '*.set']);
files_eeg = {files_eeg.name};


% Create report file:
fid = fopen([path_reports 'rejected_epos.csv'], 'a') ;
fprintf(fid, 'ID,n_epos_rejected,epos_rejected\n') ;
fclose(fid);

discarded = {};
discarded_mat = zeros(length(files_eeg),20);
counter = 0;


for isub = 1:length(files_eeg)
    %1.3 Launch EEGLAB:
    [ALLEEG EEG CURRENTSET ALLCOM] = eeglab;
    
    % 1.4 Get subj name for getting the right event file later:
    thissubject = files_eeg{isub};
    thissubject = strsplit(thissubject, mov_cond);
    thissubject = thissubject{1};    
    
    %1.5 Set filename:
    filename = strcat(thissubject, mov_cond, '_PREP_', cropstyle, '_eventsaro'); 
    filename = char(filename);
    
    %% 2.Import EEG data
    [EEG, com] = pop_loadset([path_in_eeg, filename '.set']);
    EEG = eegh(com,EEG);
    eeg_rank = rank(EEG.data);
    
    % Call helper func to reject noisy epochs:
    % arg1: EEG, arg2: threshold (in mV), arg3: manual check?
    EEG = NVR_S01_prep4ICA(EEG, 100, 0);
    
    disc_epo = find(EEG.reject.rejthresh);
    
    counter = counter+1;
    discarded_mat(counter,1:length(disc_epo)) = disc_epo;
    discarded{counter} = disc_epo;
    
    %% 5. Create and Update "Rejected epochs" list
    fid = fopen([path_reports 'rejected_epos.csv'], 'a') ;
    sub_name = strsplit(filename, '_');
    sub_name = [sub_name{1} '_' sub_name{2}];
    epos = strjoin(arrayfun(@(x) num2str(x),disc_epo,'UniformOutput',false),'-');
    c = {sub_name, ...
        sprintf('%i',length(disc_epo)), ...
        sprintf('%s', epos)};
    fprintf(fid, '%s,%s,%s\n',c{1,:}) ;
    fclose(fid);
    
       

    % run ICA:
    EEG = pop_runica(EEG, ... 
        'icatype', icatype, ... 
        'extended',1, ... 
        'interupt','on', ...
        'pca',eeg_rank);
    
    EEG = eegh(com,EEG);
    EEG.setname=filename;
    [ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG);
    EEG = pop_saveset(EEG, [filename  '_cleanICA.set'] , path_out_eeg);
    [ALLEEG EEG CURRENTSET] = eeg_store(ALLEEG, EEG);
    
    
    
        
end