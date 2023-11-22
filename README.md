# kubidCoverage

### 1. Get the depth per position
> [!NOTE]
> bam.bai should be located in the directory where the bam file is found

```
samtools depth Barcode13.bam > barcode13.depth.tsv
```


### 2. Add gene info as a new column
```
python3 addGeneInfo.py \
--inTSV barcode13.depth.tsv \
--geneTSV genes.tsv \
--outTSV barcode13.depth.genes.tsv
```


### 3. Plot the depth of coverage
```
python3 plotCoverage.py \
--inTSV barcode13.depth.genes.tsv \
--outHTML barcode13.coverage.html \
--sample barcode13
```
