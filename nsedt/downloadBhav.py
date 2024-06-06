from nsedt import reports as rep
report_date = "04-06-2024"
# date format "%d-%m-%Y"

print(rep.get_derivatives_bhav_historical_report(date=report_date, response_type="panda_df"))
