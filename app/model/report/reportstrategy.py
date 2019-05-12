import abc
from app.common.db import my_connection


'''ReportStrategyAbstract is an abstract class that contains get_reports and send_report abstract 
method in order to be implemented in the future where the ReportStrategyAbstract needed to be implemented (such 
as 'implements' in Java). '''


class ReportStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_reports(self, user_id, user_type):
        pass

    @abc.abstractmethod
    def send_report(self, user_id, patient_id, report, date):
        pass
