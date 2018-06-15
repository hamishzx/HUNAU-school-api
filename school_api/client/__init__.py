

from school_api.client.base import BaseUserClient, BaseSchoolClient
from school_api.client.api.schedule import Schedule
from school_api.client.utils import UserType, ScheduleType, NullClass

# def error_handle(func):
#     def wrapper(self):
#         try:
#             self.schedule = func(self)
#         except Exception as e:
#             print (str(e))
#             self.schedule = NullClass(str(e))
#         return self.schedule
#     return wrapper


class SchoolClient(BaseSchoolClient):

    def __init__(self, url, school_url=None):
        self.url = url
        self._login_types = [u'学生', u'教师', u'部门']
        self.login_url_suffix = '/default4.aspx'
        self.school_url = school_url or self.school_url

    def user_login(self, account, passwd, **kwargs):
        user = UserClient(self, account, passwd, **kwargs)
        return user.get_login()


class UserClient(BaseUserClient):

    schedule = Schedule()

    def __init__(self, school, account, passwd, **kwargs):
        self.account = account
        self.passwd = passwd
        self.school = school
        self.timeout = kwargs.get('timeout', 15)
        self.user_type = kwargs.get('user_type', UserType.STUDENT)
        self.schedule_type = kwargs.get('schedule_type', ScheduleType.PERSON)

    # @error_handle
    def get_login(self):
        try:
            self.login(timeout=self.timeout)
        except Exception as e:
            self.schedule = NullClass(str(e))
        return self

    # @error_handle
    # def get_schedule(self):
    #     self.schedule.get_schedule(**kwargs)
    #     return self.schedule

    def get_schedule(self, **kwargs):
        try:
            return self.schedule.get_schedule(**kwargs)
        except Exception as e:
            self.schedule = NullClass(str(e))
            return self.schedule
        return self
        