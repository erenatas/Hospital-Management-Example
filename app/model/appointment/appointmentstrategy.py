import abc


'''AppointmentStrategyAbstract is an abstract class that contains get_appointments and set_appointment abstract 
method in order to be implemented in the future where the AppointmentStrategyAbstract needed to be implemented (such 
as 'implements' in Java). '''


class AppointmentStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_appointments(self, user_):
        pass

    @abc.abstractmethod
    def set_appointment(self, doctor_id, patient_id, date):
        pass

