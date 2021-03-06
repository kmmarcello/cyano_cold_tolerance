---
title: "cold_genes_HMMs"
author: "Kaylah Marcello"
date: "1/31/2022"
output:
  html_document:
    toc: yes
    toc_float: yes
    keep_md: yes
---

# Testing Parameters for HMMs 

These are the websites and workflows I used:

[Anvio phylogenomics workflow](https://merenlab.org/2017/06/07/phylogenomics/)  
[Making your own HMM database](https://merenlab.org/2016/05/21/archaeal-single-copy-genes/)  
[HMM hits Matrix](https://anvio.org/help/main/programs/anvi-script-gen-hmm-hits-matrix-across-genomes/)  
[EggNOG database](http://eggnog5.embl.de/#/app/results)

## Making HMM file for Anvi'o (x3)
***
Custom HMM folder contains:  
genes.hmm.gz - concatenated hmm profiles from EggNOG  
genes.txt - list of genes + accession + source  
kind.txt - gene  
target.txt - AA:GENE  
noise_cutoff_terms.txt - E 1e-5, - E 1e-12, -E 1e-20  

Completed - E 1e-30, now testing stringency of noise cutoff  
HMMs downloaded from EggNOG  

### Genomes used
***
NCBI cyanobacteria whole genome sequences (WGS), filamentous  
kmrcello@farm:~/cyanobacteria/outputs/db/filamentous-subset  

## CTG various noise cutoff runs

### 1. Run HMMs from our own file, anvi-run-hmms

```bash
for i in `ls ./outputs/db/filamentous-subset/*db | awk 'BEGIN{FS=".fa"}{print $1}'`
do
  anvi-run-hmms -c $i --hmm-profile-dir hmms --just-do-it
done
```
Substitute -E 1e-5 -> -12, -20, (-30?) in hmms > noise_cutoff_terms.txt  

### 2. Use the program anvi-get-sequences-for-hmm-hits 
substitute gene name for all genes for GhostKOALA

```r
anvi-get-sequences-for-hmm-hits --external-genomes FILAMENTOUS/external-genomes-filamentous-names.tsv \
                                --hmm-source hmms \
                                --gene-names COG1278.faa.final_tree.fa \
                                -o test-params/csp-5-dna.fasta  
  
anvi-get-sequences-for-hmm-hits --external-genomes FILAMENTOUS/external-genomes-filamentous-names.tsv \
                                --hmm-source hmms \
                                --gene-names COG1278.faa.final_tree.fa \
                                --get-aa-sequence \
                                -o test-params/csp-5-aa.fasta  
```
Substitute --gene-names for corresponding gene  
Substitute -o gene-#-aa.fasta 

loop from [Anvi'o addition to anvi-get-sequences-for-hmm-hits](https://anvio.org/help/main/programs/anvi-get-sequences-for-hmm-hits/)

```r
for gene in $genes
do
    anvi-get-sequences-for-hmm-hits --external-genomes FILAMENTOUS/external-genomes-filamentous-names.tsv \
                                    --hmm-source hmms \
                                    --gene-name $gene \
                                    -o cold-gene-hmm-hits.fa/${gene}
done
```


### 3. Get table of HMM hits

```r
anvi-script-gen-hmm-hits-matrix-across-genomes --external-genomes FILAMENTOUS/external-genomes-filamentous-names.tsv \
                                               --hmm-source hmms \
                                               -o output-5.txt
```

## Output files
output-5.txt  
output-12.txt  
output-20.txt  

Genes: aceE, csp, dnaJ, hupB, recA, otsA  
aceE-5-aa.fasta  
aceE-5-dna.fasta  

aceE-12-aa.fasta  
aceE-12-dna.fasta  

aceE-20-aa.fasta  
aceE-20-dna.fasta  

## Comparing parameters
[GhostKOALA](https://www.kegg.jp/ghostkoala/)  
upload aa fasta files for each gene to compare target hits.
