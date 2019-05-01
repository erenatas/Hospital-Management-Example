from app.common.db import my_connection
from bson.json_util import dumps
from app.model.report.reportstrategy import ReportStrategyAbstract


class DoctorReportModelStrategy(ReportStrategyAbstract):

    def get_reports(self, user_id, user_type):
        appointments = my_connection.db['appointments'].find({'doctor': user_id})
        return dumps(appointments)

# def send_report(user_id, patient_id, report, date):
#     my_connection.db['report'].insert_one({
#         "doctor": user_id,
#         "patient": patient_id,
#         "report": report,
#         "date": date
#     })
#     return 'OK'
#
# def get_reports(user_id, user_type):
#     if user_type is 'Doctor':
#     if user_type is 'Patient':
#         appointments = my_connection.db['appointments'].find({'patient': user_id})
