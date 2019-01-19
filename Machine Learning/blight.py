 Your AUC of 0.58306500399 

0.756352062793

import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelEncoder




def blight_model():
    train = pd.read_csv('train.csv',encoding = 'ISO-8859-1')
    train.dropna(subset=['compliance'], how='all', inplace = True)
    y = train['compliance']

    
    
    test = pd.read_csv('test.csv',encoding = 'ISO-8859-1')
    
    test = test.fillna(value=0)
    #print (test['ticket_id'])
    #print (test['violation_zip_code'].value_counts())
    test['violator_name'] = test['violator_name'].astype(str)
    test['violation_zip_code'] = test['violation_zip_code'].astype(str)
    test['mailing_address_str_number'] = test['mailing_address_str_number'].astype(str)
    test['mailing_address_str_name'] = test['mailing_address_str_name'].astype(str)
    test['city'] = test['city'].astype(str)
    test['state'] = test['state'].astype(str)
    test['zip_code'] = test['zip_code'].astype(str)
    test['hearing_date'] = test['hearing_date'].astype(str)
    test['grafitti_status'] = test['grafitti_status'].astype(str)

    
    
    
 
    X = train[['ticket_id', 'agency_name', 'inspector_name', 'violator_name',
       'violation_street_number', 'violation_street_name',
       'violation_zip_code', 'mailing_address_str_number',
       'mailing_address_str_name', 'city', 'state', 'zip_code',
       'non_us_str_code', 'country', 'ticket_issued_date', 'hearing_date',
       'violation_code', 'violation_description', 'disposition', 'fine_amount',
       'admin_fee', 'state_fee', 'late_fee', 'discount_amount',
       'clean_up_cost', 'judgment_amount', 'grafitti_status']]
    
    
    X['violator_name'] = X['violator_name'].astype(str)
    X['violation_zip_code'] = X['violation_zip_code'].astype(str)
    X['mailing_address_str_number'] = X['mailing_address_str_number'].astype(str)
    X['mailing_address_str_name'] = X['mailing_address_str_name'].astype(str)
    X['city'] = X['city'].astype(str)
    X['state'] = X['state'].astype(str)
    X['zip_code'] = X['zip_code'].astype(str)
    X['hearing_date'] = X['hearing_date'].astype(str)
    X['grafitti_status'] = X['grafitti_status'].astype(str)
    X['non_us_str_code'] = X['non_us_str_code'].astype(str)
    
    
    le = preprocessing.LabelEncoder()
    for i in range(len(list(X.columns))):
        #print (list(X.columns)[i])
        X.iloc[:,i] = le.fit_transform(X.iloc[:,i])
    
    
    test_columns = list(test.columns)
    test_columns.remove('ticket_id')
    
    le = preprocessing.LabelEncoder()
    for i in range(1,len(list(test.columns))):
        #print (list(test.columns)[i])
        test.iloc[:,i] = le.fit_transform(test.iloc[:,i])
        
        
    
    #address = pd.read_csv('addresses.csv',encoding = 'ISO-8859-1')
    #location = pd.read_csv('latlons.csv',encoding = 'ISO-8859-1')
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    #dt = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    
    lr = LogisticRegression().fit(X_train, y_train)
    y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    print (roc_auc_lr)
    

    
    y_proba_lr = lr.fit(X_train, y_train).predict_proba(test)
    
    b = [el[1] for el in y_proba_lr]
    
    y_proba_list = b
    
    #list(zip(test['ticket_id'], b))
    ser = pd.Series(y_proba_list,index = test['ticket_id'] )
    
    
    
    return ser
           

blight_model()

-----------------------------------------------------------------------------------------


Your AUC of 0.742563590788 was awarded a value of 0.96 out of 1.0 total grades

import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier





def blight_model():
    train = pd.read_csv('train.csv',encoding = 'ISO-8859-1')
    train.dropna(subset=['compliance'], how='all', inplace = True)
    y = train['compliance']

    
    
    test = pd.read_csv('test.csv',encoding = 'ISO-8859-1')
    
    test = test.fillna(value=0)
    #print (test['ticket_id'])
    #print (test['violation_zip_code'].value_counts())
    test['violator_name'] = test['violator_name'].astype(str)
    test['violation_zip_code'] = test['violation_zip_code'].astype(str)
    test['mailing_address_str_number'] = test['mailing_address_str_number'].astype(str)
    test['mailing_address_str_name'] = test['mailing_address_str_name'].astype(str)
    test['city'] = test['city'].astype(str)
    test['state'] = test['state'].astype(str)
    test['zip_code'] = test['zip_code'].astype(str)
    test['hearing_date'] = test['hearing_date'].astype(str)
    test['grafitti_status'] = test['grafitti_status'].astype(str)

    
    
    
 
    X = train[['ticket_id', 'agency_name', 'inspector_name', 'violator_name',
       'violation_street_number', 'violation_street_name',
       'violation_zip_code', 'mailing_address_str_number',
       'mailing_address_str_name', 'city', 'state', 'zip_code',
       'non_us_str_code', 'country', 'ticket_issued_date', 'hearing_date',
       'violation_code', 'violation_description', 'disposition', 'fine_amount',
       'admin_fee', 'state_fee', 'late_fee', 'discount_amount',
       'clean_up_cost', 'judgment_amount', 'grafitti_status']]
    
    
    X['violator_name'] = X['violator_name'].astype(str)
    X['violation_zip_code'] = X['violation_zip_code'].astype(str)
    X['mailing_address_str_number'] = X['mailing_address_str_number'].astype(str)
    X['mailing_address_str_name'] = X['mailing_address_str_name'].astype(str)
    X['city'] = X['city'].astype(str)
    X['state'] = X['state'].astype(str)
    X['zip_code'] = X['zip_code'].astype(str)
    X['hearing_date'] = X['hearing_date'].astype(str)
    X['grafitti_status'] = X['grafitti_status'].astype(str)
    X['non_us_str_code'] = X['non_us_str_code'].astype(str)
    
    
    le = preprocessing.LabelEncoder()
    for i in range(len(list(X.columns))):
        #print (list(X.columns)[i])
        X.iloc[:,i] = le.fit_transform(X.iloc[:,i])
    
    
    test_columns = list(test.columns)
    test_columns.remove('ticket_id')
    
    le = preprocessing.LabelEncoder()
    for i in range(1,len(list(test.columns))):
        #print (list(test.columns)[i])
        test.iloc[:,i] = le.fit_transform(test.iloc[:,i])
        
        
    
    #address = pd.read_csv('addresses.csv',encoding = 'ISO-8859-1')
    #location = pd.read_csv('latlons.csv',encoding = 'ISO-8859-1')
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    #dt = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    
    lr = LogisticRegression().fit(X_train, y_train)
    y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    print (roc_auc_lr)
    
    
    clf = RandomForestClassifier().fit(X_train, y_train)
    k = clf.predict_proba(test)
    print (k)
    b_rf = b = [el[1] for el in k]
    

    
    y_proba_lr = lr.fit(X_train, y_train).predict_proba(test)
    
    b = [el[1] for el in y_proba_lr]
    
    y_proba_list = b
    
    #list(zip(test['ticket_id'], b))
    #ser = pd.Series(y_proba_list,index = test['ticket_id'] )
    ser = pd.Series(b_rf,index = test['ticket_id'] )
    
    
    return ser
           

blight_model()


-----------------------------------------------------------------------------------------------------

Your AUC of 0.761400208679 was awarded a value of 1.0 out of 1.0 total grades

import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC





def blight_model():
    train = pd.read_csv('train.csv',encoding = 'ISO-8859-1')
    train.dropna(subset=['compliance'], how='all', inplace = True)
    y = train['compliance']

    
    
    test = pd.read_csv('test.csv',encoding = 'ISO-8859-1')
    
    test = test.fillna(value=0)
    #print (test['ticket_id'])
    #print (test['violation_zip_code'].value_counts())
    test['violator_name'] = test['violator_name'].astype(str)
    test['violation_zip_code'] = test['violation_zip_code'].astype(str)
    test['mailing_address_str_number'] = test['mailing_address_str_number'].astype(str)
    test['mailing_address_str_name'] = test['mailing_address_str_name'].astype(str)
    test['city'] = test['city'].astype(str)
    test['state'] = test['state'].astype(str)
    test['zip_code'] = test['zip_code'].astype(str)
    test['hearing_date'] = test['hearing_date'].astype(str)
    test['grafitti_status'] = test['grafitti_status'].astype(str)

    
    
    
 
    X = train[['ticket_id', 'agency_name', 'inspector_name', 'violator_name',
       'violation_street_number', 'violation_street_name',
       'violation_zip_code', 'mailing_address_str_number',
       'mailing_address_str_name', 'city', 'state', 'zip_code',
       'non_us_str_code', 'country', 'ticket_issued_date', 'hearing_date',
       'violation_code', 'violation_description', 'disposition', 'fine_amount',
       'admin_fee', 'state_fee', 'late_fee', 'discount_amount',
       'clean_up_cost', 'judgment_amount', 'grafitti_status']]
    
    
    X['violator_name'] = X['violator_name'].astype(str)
    X['violation_zip_code'] = X['violation_zip_code'].astype(str)
    X['mailing_address_str_number'] = X['mailing_address_str_number'].astype(str)
    X['mailing_address_str_name'] = X['mailing_address_str_name'].astype(str)
    X['city'] = X['city'].astype(str)
    X['state'] = X['state'].astype(str)
    X['zip_code'] = X['zip_code'].astype(str)
    X['hearing_date'] = X['hearing_date'].astype(str)
    X['grafitti_status'] = X['grafitti_status'].astype(str)
    X['non_us_str_code'] = X['non_us_str_code'].astype(str)
    
    
    cols = ['ticket_id', 'fine_amount',
        'discount_amount'
       ]
    
    
    #X= X[cols]
    #test = test[cols]
    
    
    
    
    le = preprocessing.LabelEncoder()
    for i in range(len(list(X.columns))):
        #print (list(X.columns)[i])
        X.iloc[:,i] = le.fit_transform(X.iloc[:,i])
    
    
    test_columns = list(test.columns)
    test_columns.remove('ticket_id')
    
    le = preprocessing.LabelEncoder()
    for i in range(1,len(list(test.columns))):
        #print (list(test.columns)[i])
        test.iloc[:,i] = le.fit_transform(test.iloc[:,i])
        
        
    
    #address = pd.read_csv('addresses.csv',encoding = 'ISO-8859-1')
    #location = pd.read_csv('latlons.csv',encoding = 'ISO-8859-1')
    
    
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    #dt = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
    
    
    #Using logical regressin
    lr = LogisticRegression().fit(X_train, y_train)
    y_score_lr = lr.fit(X_train, y_train).decision_function(X_test)
    fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    print (roc_auc_lr)
    y_proba_lr = lr.fit(X_train, y_train).predict_proba(test)
    b = [el[1] for el in y_proba_lr]
    y_proba_list = b
    #ser = pd.Series(y_proba_list,index = test['ticket_id'] )
    
    
    #Using Random Forest Classifier
    clf = RandomForestClassifier().fit(X_train, y_train)
    #decision function is not supported for random forest
    k = clf.predict_proba(test)
    b_rf = b = [el[1] for el in k]
    #Calculate roc_auc
    y_score = clf.predict(X_test)
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    print('AUC Random Forest classifier: {:.2f}'.format(roc_auc))
    #ser = pd.Series(b_rf,index = test['ticket_id'] )
    
    
    #Using Gradient-boosted decision trees
    clf = GradientBoostingClassifier().fit(X_train, y_train)
    k = clf.predict_proba(test)
    gr_rf  = [el[1] for el in k]
    #Calculate roc_auc
    y_score = clf.predict(X_test)
    fpr, tpr, _ = roc_curve(y_test,y_score)
    roc_auc = auc(fpr, tpr)
    print('Gradient boost classifier: {:.2f}'.format(roc_auc))
    ser = pd.Series(gr_rf,index = test['ticket_id'] )   
    
    '''
    #Using SVC - taking too long
    print ("here")
    clf = SVC(kernel='rbf', C=1, probability=True).fit(X_train, y_train)
    print ("here")
    k = clf.predict_proba(test)
    gr_rf  = [el[1] for el in k]
    #Calculate roc_auc
    y_score = clf.predict(X_test)
    fpr, tpr, _ = roc_curve(y_test,y_score)
    roc_auc = auc(fpr, tpr)
    print('Gradient boost classifier: {:.2f}'.format(roc_auc))
    '''
  
   
    #ser = pd.Series(gr_rf,index = test['ticket_id'] )
    
    
    return ser
           

blight_model()
