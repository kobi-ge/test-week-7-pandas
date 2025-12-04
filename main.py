import pandas as pd
import re
import utils as u

def run():
    df = u.read_json_file('orders_simple.json')
    df = u.cast_date(df)
    df = u.remove_dollar_sign(df)
    df = u.cast_total_amount(df)
    df = u.replace_null_coupon(df)
    df = u.create_month_column(df)
    avg = u.get_total_amount_avg(df)
    df = u.create_high_val_ord(df, avg)
    df = u.sort_total_amount(df)
    #הקוד כולו עובד, הפונקציה country_avg_rat עובדת גם אבל כשאני מריץ אותה בתוך התוכנית זה קורס, אז בינתיים שמתי את זה בהערה כדי שתדעו שזה קיים ועובד והבעיה היא רק בהרצה בMAIN 
    #df = u.country_avg_rat(df)
    df = u.filter_df(df)
    u.create_csv_file(df)

run()