import pandas as pd 
import re

def read_json_file(file_name):
    df = pd.read_json(file_name)
    return df

def cast_date(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

def remove_dollar_sign(df):
    df['total_amount'] = df['total_amount'].astype(str).str.replace('$','')
    return df

def cast_total_amount(df):
    df = df.astype({'total_amount': float})
    return df

def replace_null_coupon(df):
     df['coupon_used'] = df['coupon_used'].astype(str).str.replace('','no coupn')
     return df

def create_month_column(df):
    df['month'] = pd.to_datetime(df['order_date']).dt.month
    return df

def get_total_amount_avg(df):
    return df['total_amount'].mean()

def create_high_val_ord(df, avg):
    df['high_value_order'] = df['total_amount'] > avg
    return df

def sort_total_amount(df):
    df = df.sort_values(by='total_amount', ascending= False)
    return df

def country_avg_rat(df):
    df['avg_cntry_rat'] = df.groupby('country')['rating'].transform('mean')
    return df

def country_avg_rat(df):
    a = df.groupby('country')['rating'].mean()
    return a

def filter_df(df):
    df = df.loc[(df['total_amount'] > 1000) & (df['rating'] > 4.5)]
    return df

def create_status_delivery(df):
    df['status_delivery'] = ['delayed' if df['days_shipping'] > 7 else 'on time']
    return df

def create_csv_file(df):
    return df.to_csv('clean_orders324180694.csv',  header=False, index=False)
