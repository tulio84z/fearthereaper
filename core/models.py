from django.db import models

class Week(models.Model):
    PAST_WEEK_BEFORE_SIGNUP = 'PWBS'
    PAST_WEEK_NO_OBJ = 'PWNO'
    PAST_WEEK_MISSED_OBJ = 'PWMO'
    PAST_WEEK_OBJ_ACHIEVED = 'PWOA'

    CURRENT_WEEK_NO_OBJ = 'CWNO'
    CURRENT_WEEK_WITH_OBJ = 'CWWO'
    CURRENT_WEEK_OBJ_ACHIEVED = 'CWOA'

    FUTURE_WEEK_NO_OBJ = 'FWNO'
    FUTURE_WEEK_WITH_OBJ = 'FWWO'

    WEEK_STATUSES = (
        (PAST_WEEK_BEFORE_SIGNUP, 'Past week before singup'),
        (PAST_WEEK_NO_OBJ, 'Past week no objective'),
        (PAST_WEEK_MISSED_OBJ, 'Past week missed objective'),
        (PAST_WEEK_OBJ_ACHIEVED, 'Past week objective achieved'),

        (CURRENT_WEEK_NO_OBJ, 'Current week no objective'),
        (CURRENT_WEEK_WITH_OBJ, 'Current week with objective'),
        (CURRENT_WEEK_OBJ_ACHIEVED, 'Current week objective achieved'),

        (FUTURE_WEEK_NO_OBJ, 'Future week no objective'),
        (FUTURE_WEEK_WITH_OBJ, 'Future week with objective'),
    )

    week_status = models.CharField(
        max_length=4,
        choices=WEEK_STATUSES,
        blank=True,
    )

class Objective(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    objective_achieved = models.BooleanField(default=False)
