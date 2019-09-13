library(tidyverse)

df <- read.csv('../../../apathy/RUNDMC_data/RUNDMC_long_normed.csv') %>%
    mutate(intercept = 1) %>%
    subset(TP==2011) %>%
    drop_na(FA_kurtosis_AllWM, CESDtotal, AEStotal)

paste(sprintf('%.3d', df$ID), '_mod_8mm.nii.gz', sep='')


df %>%
    select(intercept, age, AEStotal) %>%
    write.table('design.txt', sep='\t', col.names=F, row.names=F, quote=F)
