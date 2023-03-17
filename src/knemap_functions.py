import pandas as pd




def update_dataframe_indexes(df, mapping):
    '''
    Updates the index of df with keys of mapping.

    Input

        df (DataFrame)

        mapping (dict): key needs to be same as index identifiers of data_genes, as loaded from file

    Output

        df (DataFrame)
    '''
    temp = df.index.tolist()
    new_indx = []
    for item in temp:
        if item in mapping.keys():
            new_indx.append(str(mapping[item]))
        else:
            new_indx.append(item)
        
    df.index = new_indx
    return df




def remove_unknown_genes(mapping, data_genes):
    
    '''
    Drops genes (row identifiers) from data_genes that are not in mapping
    
    Input:

        mapping (dict): key needs to be same as index identifiers of data_genes, as loaded from file

        data_genes (dataFrame): as loaded from file, processed gene expression data. Indices need to be gene identifiers.
        
    Output:

        data (dataFrame): only containing genes were data is known about
    '''
    
    #select all rows which data is known for
    print("original number of rows ", len(data_genes))
    
    for gene in data_genes.index:
        if gene not in mapping.keys():
            data_genes = data_genes.drop(gene)
    
    print("number of known genes ", len(data_genes))
    
    
    
    
    return data_genes

def select_genes(chemical_genes, top=100, bottom=100, sort_by=None):
    '''
    
    helper function of create_fingerprints()
    
    
    Input

        chemical_genes (DataFrame) with single colum, were index is gene names and colum FC for specific chemical

        top / bottom (int) specifiy x top & bottom affect genes should be selected

        sort_by (str) is name of column dataFrame is sorted after (chemical name)
    
    Output

         df (dataFrame) with selected genes and FC values
    
    
    '''
    
    #sort dataframe after column values
    if sort_by is not None:
        sorted_frame = chemical_genes.sort_values(by=[sort_by], ascending=False)
        
        #select top and bottom rows to be returned
        top_frame = sorted_frame.head(top)
        bottom_frame = sorted_frame.tail(bottom)
        
        
        #merge back together into single frame
        return pd.concat([top_frame, bottom_frame], sort=True)
        
        
        
        
    else:
        print("please specify column name to sort by")
        return None
    
    
def get_partitioning_id(partitioning):
    '''
    helper function of create_fingerprints()

    Input

        partitioning (dict): communities, as loaded from file

    Output

        l (list)
    '''
    l = []
    
    for i in partitioning.values():
        if len(i) > 0:
            if i[0] not in l:
                l.append(i[0])
        
            
    return l


def create_fingerprints(partitioning, df, top=100, bottom=100, add=""):
    '''
    main mapping function to create exposure fingerprints via network mapping
    
    Input

        partitioning (dict): communities, as loaded from file

        df (dataFrame): exsposure data to select genes from. Each column needs to be an exposure, index needs to be same identifiers as partitioning values and individual genes will be ranked by values of each column.
        
        top (int): # of top ranked genes to be selected for each exposure
        
        bottom (int): # of bottom ranked genes to be selected for each exposure
        
        add (str): suffix to be added to column identifiers. This is needed if multiple exposures with same column names are compared
        
     Output

         fingerprint (dict): key is column identifier + suffix and value is fingerprint (list)
    '''
    fingerprint = {}
    
    #get ids of partitionings
    part = get_partitioning_id(partitioning)
    
    for c in df.columns:
        #print(c)
        temp = {}
        for i in part:
            temp[i] = 0
            
            
        #get top & bottom gene for chemical c
        current = df[[c]]
        cur = select_genes(current, top=top, bottom=bottom, sort_by=c)
        
        #map genes to their communities
        for gene in cur.index:
            #get its community id
            if gene in partitioning.keys():
                com = partitioning[gene][0]
                #add to temp
                temp[com] = temp[com] + 1
            else:
                print(gene)
        #update temp to fraction
        for key in temp.keys():
            x = temp[key]
            temp[key] = x / (top+bottom)
            
        #print(temp)
        fingerprint[c+add] = temp
        
    return fingerprint


    
def sort_fingerprint_by_key(fingerprint):
    '''
    sorts the fingerprints by key so that if multiple data sets are compared, they can be in the same order
    
    Input

        fingerprint (dict): as returned by create_fingerprints()
        
    Output
    
        sorted fingerprint (dict): fingerprint sorted by key
    
    '''
    fingerprint_new = {}

    for k in fingerprint:
        fingerprint_new[k] = {}
        keylist = list(fingerprint[k].keys())
        keylist.sort()

        for key in keylist:
            fingerprint_new[k][key] = fingerprint[k][key]
            
            
    return fingerprint_new
