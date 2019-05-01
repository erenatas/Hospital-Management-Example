import abc
from app.common.db import my_connection


class ReportStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_reports(self, user_id, user_type):
        pass

    def send_report(self, user_id, patient_id, report, date):
        my_connection.db['report'].insert_one({
            "doctor": user_id,
            "patient": patient_id,
            "report": report,
            "date": date
        })
        return 'OK'
