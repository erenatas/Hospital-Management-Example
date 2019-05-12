from app.common.db import my_connection
from bson.json_util import dumps
from app.model.report.reportstrategy import ReportStrategyAbstract


'''
DoctorReportModelStrategy implements get_reports and send_report methods for the Doctor. 
'''


class DoctorReportModelStrategy(ReportStrategyAbstract):

    def get_reports(self, user_id, user_type):
        reports = my_connection.db['report'].find({'doctor': user_id})
        return dumps(reports)

    def send_report(self, user_id, patient_id, report, date):
        my_connection.db['report'].insert_one({
            "doctor": user_id,
            "patient": patient_id,
            "report": report,
            "date": date
        })
        return 'OK'
