# KNeMAP: A Network Mapping Approach for Knowledge-driven Comparison of Transcriptomic Profiles

This is the accompanying code for the publication KNeMAP: A Network Mapping Approach for Knowledge-driven Comparison of Transcriptomic Profiles by Pavel et al.

## Abstract

Transcriptomic data are used to describe a compound’s mechanism of action. However, they are complex and prone to noise, making the comparison of different datasets challenging. Often, transcriptomic profiles are compared at the level of individual gene expression values, or sets of differentially expressed genes. Such approaches can be prone to underlying technical and biological variance, such as the biological system exposed on or the machine/ method used to measure gene expression data, technical errors and further neglect the relationships between the genes. Therefore, we propose a network mapping approach for knowledge-driven comparison of transcriptomic profiles (KNeMAP), which combines genes into similarity groups based on multiple levels of prior information, hence adding a higher level view onto the individual gene view. When comparing KNeMAP with fold change (expression) based and deregulated gene set based methods, KNeMAP was able to group compounds with higher accuracy with respect to prior information as well as is less prone to noise corrupted data.
We applied KNeMAP to the Connectivity Map dataset, where the gene expression changes of three cell lines were analyzed after treatment with 676 drugs. Although the expression profiles across the biological systems are highly different, KNeMAP identified a set of 38 compounds that induce similar molecular responses when used as treatment on the same biological system.

## Files

/data/HL60_small.csv - the pre-processed expression data (FC) of the CMAP HL60 cells, as described in the manuscript. This file only contains 50 drugs, the complete file can be found on Zenodo.

/data/MCF7_small.csv - the pre-processed expression data (FC) of the CMAP MCF7 cells, as described in the manuscript. This file only contains 50 drugs, the complete file can be found on Zenodo.

/data/PC3_small.csv - the pre-processed expression data (FC) of the CMAP PC3 cells, as described in the manuscript. This file only contains 50 drugs, the complete file can be found on Zenodo.

/data/communities.csv - community assignment of the prior network nodes; the IDs can be mapped to Ensembl IDs via /data/prior_gene_mapping.txt

/data/prior_graph.csv - edge list of the prior network; the IDs can be mapped to Ensembl IDs via /data/prior_gene_mapping.txt

/data/prior_gene_mapping.txt - JSON where keys are Ensembl_IDs and values are network node IDs

main.ipynb - main script to map expression data to prior network & generate exposure fingerprint vectors

/src/mapping_functions.py - functions called in script_for_publication.ipynb

## Dependencies
- pandas
- json






