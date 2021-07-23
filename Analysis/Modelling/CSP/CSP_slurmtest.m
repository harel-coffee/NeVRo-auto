function CSP_slurm_array(jobID)

distcomp.feature( 'LocalUseMpiexec', false )

ncpus = str2num(getenv('SLURM_CPUS_PER_TASK'));
parpool('local', ncpus)

addpath(genpath('/raven/ptmp/fklotzsche/Software/BCILAB/'))
addpath(genpath('/raven/ptmp/fklotzsche/Experiments/Nevro/'))

ids = {};
for i=1:44
    if i <10
        ss = sprintf('NVR_S0%i', i);
    else
        ss = sprintf('NVR_S%i', i);
    end
    ids{end+1} = {ss};
end

parfor i=1:44
    id = ids{i}
    NVR_08_CSP_permutations_batch('SBA', 'mov', 'subject_subset', id, 'smote', true) 
end