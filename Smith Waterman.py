#Assigment 1

import pandas as pd
import numpy as np 

def smithWatermann(seq1,seq2):
    #scoring scheme
    is_match = int(input("Enter the matching score: "))
    is_mismatch = int(input("Enter the mismatch score: "))
    gap = int(input("Enter the gap penalty: "))

    row_label = [""] + list(seq1)
    col_label = [""] + list(seq2)

    df = pd.DataFrame(np.zeros(( len(seq1) + 1, len(seq2) + 1), dtype = int), index = row_label, columns= col_label)
    traceback = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype = str)
    
    # matrix initialization
    for i in range(len(df.columns)):
        df.iloc[0,i] = 0
        traceback[0,i] = ''

    for j in range(len(df.index)):
        df.iloc[j,0] = 0
        traceback[j,0] = ''
    
    # matrix filling
    max_score = 0
    position = (0,0)

    for j in range(1,len(df.index)):
        for i in range(1,len(df.columns)):
            up = max(0, df.iloc[ j - 1, i] + gap)
            left = max(0, df.iloc[j, i - 1] + gap)
            diag = max(0, df.iloc[ j - 1, i - 1] + (is_match if df.index[j] == df.columns[i] else is_mismatch))

            df.iloc[j,i] = max(diag, up, left, 0)

            if df.iloc[j,i] > max_score:
                max_score = df.iloc[j,i]
                position = (j,i) 
            
            if df.iloc[j,i] == diag:
                traceback[j,i] = '↖'
            
            elif df.iloc[j,i] == up:
                traceback[j,i] ='↑'
            
            else:
                traceback[j,i] = '←'

    #traceback
    aligned_seq1  = ''
    aligned_seq2 = '' 
    aligment = ''
    
    j, i = position
    
    while j >0  or i > 0:
        if j >0 and i >0 and traceback[j,i] == '↖':
            aligned_seq1 = seq1[j-1] + aligned_seq1
            aligned_seq2 = seq2[i-1] + aligned_seq2
            aligment = ('|' if seq1[j - 1] == seq2[i-1] else '*') + aligment
            j -= 1
            i -= 1
        
        elif j >0 and traceback[j, i] == '↑':  
            aligned_seq1 = seq1[j - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            aligment = '-' + aligment
            j -= 1

        elif i > 0 and traceback[j, i] == '←':  
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[i - 1] + aligned_seq2
            aligment = ' ' + aligment
            i -= 1
    
    print('Score matrix: ')
    print()
    print(df)
    print()
    print('Aligment: ', aligned_seq1)
    print('          ', aligment)
    print('          ', aligned_seq2)
    print('Score: ',max_score)

    return ''

sequence_1 = input(str("Enter the first sequence: ")).upper()
sequence_2 = input(str("Enter the second sequence: ")).upper()
print('Seq1:', sequence_1, 'Seq2:', sequence_2)
print()
print(smithWatermann(sequence_1,sequence_2))

