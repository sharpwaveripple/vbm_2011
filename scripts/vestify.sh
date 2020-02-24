#!/usr/bin/env bash

for i in $(ls matrices/*.txt); do
    filename=$(echo $i | cut -d'/' -f2)
    basename=$(echo $filename | cut -d'.' -f1)
    Text2Vest $i matrices/$basename.mat
done

for i in $(ls contrasts/*.txt); do
    filename=$(echo $i | cut -d'/' -f2)
    basename=$(echo $filename | cut -d'.' -f1)
    Text2Vest $i contrasts/$basename.con
done
