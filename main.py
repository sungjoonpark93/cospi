import pandas as pd

#read gene expression data
gex_file = "./data/exp/prostate1_geneMatrix.tsv"
df = pd.read_csv(gex_file,sep='\t',index_col=0)

#read context label data
with open("./data/exp/prostate_context_label.tsv",'r') as r:
    for line in r:
        context_label_list = line.strip().split("\t")

#read pathway data (KEGG, NCI-PID, reactome), dict
# pathway = dict{'readtome : ['a','b','c']}


#significant_genes = (Sereies : index : genes , values: pvalue)
#enriched_pathway ={Series : index : pathway, values: p value}
#COSPI =  {dict: {'pathway id:df(pathway interaction ranking)}}

