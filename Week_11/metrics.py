import numpy as np

def completeness_purity(true_value, prediction):
    
    number_total_qso = len(np.where(true_value==1)[0])
    number_of_qso_as_qso = len(np.where((true_value==1) & (prediction==1))[0])
    number_of_qso_as_not_qso = len(np.where((true_value==1) & (prediction==0))[0])

    number_pred_qso = len(np.where(prediction==1)[0])
    #number_of_pred_as_qso = len(np.where((true_value==0) & (prediction==1))[0])
    
    
    #print('Number of total true QSO',number_total_qso)
    #print('Number of true QSO as predicted as QSO',number_of_qso_as_qso)
    #print('Number of true QSO not QSO',number_of_qso_as_not_qso)
    #print('Number of total predicted QSO',number_pred_qso)
    #print('Number of predicted QSO not QSO',number_of_pred_as_qso)
    
    completeness = number_of_qso_as_qso*1.0/number_total_qso
    purity = number_of_qso_as_qso*1.0/number_pred_qso
    return completeness, purity