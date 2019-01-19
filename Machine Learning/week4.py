def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    col = ["State", "RegionName"]
    df = pd.read_table('university_towns.txt',error_bad_lines=False,header=None)
    #print (df)
   
    df["State"] =""
    df = df.rename(columns={0: "RegionName"})
    df['State'] = df['RegionName']
    cols = df.columns.tolist()
     
    cols = cols[-1:] + cols[:-1]
     
    df = df[cols]
    df.loc[~df['State'].str.contains('edit'),'State'] = ""
    df['State'] = df['State'].str.replace('\[.*','')
    
    
    df['RegionName'] = df['RegionName'].str.replace('\[.*','')
    df['RegionName'] = df['RegionName'].str.replace(r" \(.*","")
    
    df['RegionName'] = df['RegionName'].str.replace('\n','')
    
    for i, row in df.iterrows():
       
        if (row['State'])!="":
            st = row['State']
        else:
            row['State'] = st
        
    for i, row in df.iterrows():
         if (row['State'])==(row['RegionName']):
            row['RegionName'] = np.NaN
            
    #df = df[pd.notnull(df['RegionName'])] 
    df.dropna(subset=['RegionName'], how='all', inplace = True)
    df = df.reset_index(drop=True)
    
    
    
    
    print('Shape test: ', "Passed" if df.shape ==
      (517, 2) else 'Failed')
    print (df.index.tolist())
    print('Index test: ',
      "Passed" if df.index.tolist() == list(range(517))
      else 'Failed')
    
    print('Column test: ',
      "Passed" if df.columns.tolist() == cols else 'Failed')
    print('\\n test: ',
      "Failed" if any(df[cols[0]].str.contains(
          '\n')) or any(df[cols[1]].str.contains('\n'))
      else 'Passed')
    print('Trailing whitespace test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\s+$')) or any(df[cols[1]].str.contains(
              '\s+$'))
      else 'Passed')
    print('"(" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\(')) or any(df[cols[1]].str.contains(
              '\('))
      else 'Passed')
    print('"[" test:',
      "Failed" if any(df[cols[0]].str.contains(
          '\[')) or any(df[cols[1]].str.contains(
              '\]'))
      else 'Passed')
    return df


get_list_of_university_towns()
