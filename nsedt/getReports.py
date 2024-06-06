from nsedt import reports as rep
report_date = "04-06-2024"
# date format "%d-%m-%Y"

print(rep.get_market_activity_report(date=report_date))
print(rep.get_bhav_copy_zip(date=report_date, response_type="json"))
print(rep.get_sec_full_bhav_copy(date=report_date, response_type="json"))
print(rep.get_volatility_report(date=report_date, response_type="json"))
print(rep.get_fno_participant_wise_oi_data(date=report_date, response_type="json"))
print(rep.get_fno_participant_wise_volume_data(date=report_date, response_type="json"))