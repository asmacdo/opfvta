from samri.report.registration import measure_sim

mi = measure_sim('data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz','data/vta_projection_tstat.nii.gz')
print(mi)
