%% Run the preprocessing pipeline
%2018 by Felix Klotzsche
% work in progress - first steps missing

NVR_path = genpath('..\..\..\NeVRo');
addpath(NVR_path);

m_conds = {'nomov'}; % {'mov'}; % {'mov' 'nomov'}; %
c_styles = {'SBA'}; %{'SBA', 'SA'};

for mc=1:numel(m_conds)
    for cs = 1:numel(c_styles)
        %NVR_03_crop(c_styles{cs},m_conds{mc});%('SBA','mov')
        %NVR_04_eventsARO(c_styles{cs},m_conds{mc});%('SBA','mov')
        %NVR_05_ICA(c_styles{cs},m_conds{mc});
        %NVR_06_rejcomp(c_styles{cs},m_conds{mc});
    end
end