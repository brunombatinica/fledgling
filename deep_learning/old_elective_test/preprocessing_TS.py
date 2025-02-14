'''
July 2023 by Bruno Batinica
Modelled on code written by Sebastiano Barbieri
s.barbieri@unsw.edu.au
https://www.github.com/sebbarb/
'''

import feather
import pandas as pd
from hyperparameters import Hyperparameters

from pdb import set_trace as bp


def main():
    hp = Hyperparameters()
    
    df = feather.read_dataframe(hp.data_dir + '/raw_data/TESTSAFE0913.feather')
    
    #chose how to cut them up
    bp()

    #convert result date to month index and remove
    def month_ind(x):
        date_y = datetime.strptime("2009-01-01","%Y-%m-%d")
        date_x = datetime.strptime(x,"%Y-%m-%d")
        total_months = (date_x.year - date_y.year) * 12 + date_x.month - date_y.month
        return(total_months)
    df["dispmonth_index"] = [month_ind(i) for i in ts_df["RESULT_DATE"].astype(str)]
    df['dispmonth_index'] = df['dispmonth_index'].astype(int)
    df.drop("RESULT_DATE",inplace = True)
    
    #Discretize results into groups
    #using .apply 
    def discretize(test,result):
        #base number to code ontop of - an be anything
        e = 0#271828
        if test == "egfr":
            if result < 30.0:
                return e + 1
            elif result >= 30.0 and result < 45.0:
                return e + 2
            elif result >= 45.0 and result < 60.0:
                return e + 3
            elif result >= 60.0 and result < 90.0:
                return e + 4
            elif result > 90.0:
                return e + 5
        
        elif test == "hba1c":
            if result < 40.0:
                return e + 10 + 1
            elif result >= 40.0 and result < 50:
                return e + 10 + 2
            elif result >= 50.0 and result < 55:
                return e + 10 + 3
            elif result >= 55.0 and result < 65:
                return e + 10 + 4
            elif result >= 65.0 and result < 80:
                return e + 10 + 5
            elif result >= 80.0 and result < 100:
                return e + 10 + 5
            elif result >= 100:
                return e + 10 + 5

        elif test == "tchdl":
            if result < 4.5:
                return e + 20 + 1
            elif result >= 4.5:
                return e + 20 + 2
    #applying function
    df.apply()

    #remove duplicates - always good to do
    df.drop_duplicates(inplace=True)

    print('Remove future data...')
    df = df[df['dispmonth_index'] < 60]
    
    print('Split males and females...')
    males = feather.read_dataframe(hp.data_pp_dir + 'Py_VARIANZ_2012_v3-1_pp_males.feather')['VSIMPLE_INDEX_MASTER']
    females = feather.read_dataframe(hp.data_pp_dir + 'Py_VARIANZ_2012_v3-1_pp_females.feather')['VSIMPLE_INDEX_MASTER']
    df_males = df.merge(males, how='inner', on='VSIMPLE_INDEX_MASTER')
    df_females = df.merge(females, how='inner', on='VSIMPLE_INDEX_MASTER')

    print('Remove codes associated with less than min_count persons...')
    df_males = df_males[df_males.groupby('chem_id')['VSIMPLE_INDEX_MASTER'].transform('nunique') >= hp.min_count]
    df_females = df_females[df_females.groupby('chem_id')['VSIMPLE_INDEX_MASTER'].transform('nunique') >= hp.min_count]

    print('Code prevalence and most frequent diag type...')
    info_ph_males = df_males.groupby(['chem_id'])['VSIMPLE_INDEX_MASTER']
    info_ph_males = info_ph_males.agg(lambda x: x.nunique()).to_frame().reset_index()
    info_ph_males.rename(columns={'VSIMPLE_INDEX_MASTER': 'PREVALENCE'}, inplace=True)
    info_ph_females = df_females.groupby(['chem_id'])['VSIMPLE_INDEX_MASTER']
    info_ph_females = info_ph_females.agg(lambda x: x.nunique()).to_frame().reset_index()
    info_ph_females.rename(columns={'VSIMPLE_INDEX_MASTER': 'PREVALENCE'}, inplace=True)
    
    print('Save...')
    info_ph_males.to_feather(hp.data_pp_dir + 'info_ph_males.feather')
    info_ph_females.to_feather(hp.data_pp_dir + 'info_ph_females.feather')      
    
    df_males.sort_values(by=['VSIMPLE_INDEX_MASTER', 'dispmonth_index', 'chem_id'], ascending=True, inplace=True)
    df_males.reset_index(drop=True, inplace=True)
    df_males.to_feather(hp.data_pp_dir + 'PH_pp_males.feather')

    df_females.sort_values(by=['VSIMPLE_INDEX_MASTER', 'dispmonth_index', 'chem_id'], ascending=True, inplace=True)
    df_females.reset_index(drop=True, inplace=True)
    df_females.to_feather(hp.data_pp_dir + 'PH_pp_females.feather')


if __name__ == '__main__':
    main()
    