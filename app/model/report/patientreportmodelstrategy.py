from app.common.db import my_connection
from bson.json_util import dumps
from app.model.report.reportstrategy import ReportStrategyAbstract


'''
PatientReportModelStrategy implements get_reports and send_report methods for the Patient. 
'''


class PatientReportModelStrategy(ReportStrategyAbstract):

    def get_reports(self, user_id, user_type):
        appointments = my_connection.db['report'].find({'patient': user_id})
        return dumps(appointments)

    def send_report(self, user_id, patient_id, report, date):
        return 'Error, a patient cannot send reports.'
