from samri.report.registration import measure_sim

cc = measure_sim('data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz','data/vta_projection_tstat.nii.gz',
        sampling_percentage=1.0,
        metric='CC',
        mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
        )
gc = measure_sim('data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz','data/vta_projection_tstat.nii.gz',
        sampling_percentage=1.0,
        metric='GC',
        mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
        )
mi = measure_sim('data/l2/alias-block_filtered_controlled/acq-EPI_tstat.nii.gz','data/vta_projection_tstat.nii.gz',
        radius_or_number_of_bins=32,
        sampling_percentage=1.0,
        metric='MI',
        mask='/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii',
        )

out_str = 'CC={cc}, GC={gc}, MI={mi}'.format(
        cc=cc['similarity'],
        gc=gc['similarity'],
        mi=mi['similarity'],
        )

print(out_str)
