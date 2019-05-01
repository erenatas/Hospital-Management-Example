from app.common.db import my_connection
from bson.json_util import dumps
from app.model.report.reportstrategy import ReportStrategyAbstract


class PatientReportModelStrategy(ReportStrategyAbstract):

    def get_reports(self, user_id, user_type):
        appointments = my_connection.db['appointments'].find({'patient': user_id})
        return dumps(appointments)