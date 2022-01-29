from datetime import datetime as dt
from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        now = dt.now().hour
        if now >= 3 and now <= 5:
            return False
        return True 