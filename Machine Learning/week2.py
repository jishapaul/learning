def answer_one():
    series =  (df['Gold'])
    #print (series)
    mx = 0
    country = "None"
    for key in series.keys():
        if  (series[key]) > mx:
            mx = series[key]
            country = key
            #print (country+" "+str(mx))
    return country
answer_one()




def answer_two():
    series_gold_summer = (df['Gold'])
    series_gold_winter = (df['Gold.1'])
    mx = 0
    country = "None"
    for key in series_gold_summer.keys():
        summer = series_gold_summer[key]
        winter = series_gold_winter[key]
        if summer-winter > mx:
            mx = summer-winter
            country = key
            #print (country+" "+str(summer)+" "+str(winter))
    return country
answer_two()

def answer_three():
    series_gold_summer = (df['Gold'])
    series_gold_winter = (df['Gold.1'])
    series_gold_total = (df['Gold.2'])
    mx = 0
    country = "None"
    for key in series_gold_summer.keys():
        summer = series_gold_summer[key]
        winter = series_gold_winter[key]
        if summer==0 or winter==0:
            continue
        total = series_gold_total[key]
        if total==0:
                continue
        if float(summer-winter)/total > mx:
            mx = float(summer-winter)/total 
            country = key
            #print (country+" "+str(summer)+" "+str(winter))
    #print (type(country))
    return country
answer_three()  

def answer_four():
    df1 = df.copy()
    df1['Points'] = df1['Gold.2']*3+ df1['Silver.2']*2+df1['Bronze.2']
    return df1['Points']
answer_four()

def answer_five():
    df1 = census_df.copy()
    #print (df1)
    p = df1['STNAME'].value_counts().argmax()
    print (p)
    return p
answer_five()

def answer_six():
    df1 = census_df.copy()
    df1=df1[df1['SUMLEV'] == 50]
    df1 = df1[['STNAME','CTYNAME','CENSUS2010POP']]
    states = (df1['STNAME'].unique())
    dict={}
    for state in states:
        k = df1.sort_values(by=['CENSUS2010POP'],ascending=False)[df1['STNAME']==state][0:3].sum()
        curr_val =  ((k['CENSUS2010POP'])) 
        dict[state] = curr_val
    #print (dict)
    series = pd.Series(dict).sort_values(ascending=False)[0:3]
    print (type(series.index.tolist()))
    
    return series.index.tolist()
answer_six()


def answer_seven():
    df1 = census_df.copy()
    df1=df1[df1['SUMLEV'] == 50]
    df1 = df1[['STNAME','CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012',
               'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']]
    #print ((df1))
    d = 0
    country = ""
    for x in range(0,len(df1)):
        mx =  (max([df1.iloc[x]['POPESTIMATE2010'],df1.iloc[x]['POPESTIMATE2011'],df1.iloc[x]['POPESTIMATE2012'],df1.iloc[x]['POPESTIMATE2013'],df1.iloc[x]['POPESTIMATE2014'],df1.iloc[x]['POPESTIMATE2015'] ]))
        mn =  (min([df1.iloc[x]['POPESTIMATE2010'],df1.iloc[x]['POPESTIMATE2011'],df1.iloc[x]['POPESTIMATE2012'],df1.iloc[x]['POPESTIMATE2013'],df1.iloc[x]['POPESTIMATE2014'],df1.iloc[x]['POPESTIMATE2015'] ]))
        diff = mx-mn
        
        #print (diff)
        if diff > d:
            d = diff
            country =  (df1.iloc[x]['CTYNAME'])
        #print (str(mx) + "  "+str(mn))
    return country
    
answer_seven()

def answer_eight():
    df1 = census_df.copy()
   
    df1 = df1[(df1['REGION'] < 3) & (df1['POPESTIMATE2015']>df1['POPESTIMATE2014']) & (df1['CTYNAME'].str.startswith('Washington', na=False)    )     ]
    df1 = df1[['STNAME', 'CTYNAME']]
    
    # & (df1['CTYNAME'][0:2]==list['Wa']]
    print (type(df1))
    return df1
answer_eight()

