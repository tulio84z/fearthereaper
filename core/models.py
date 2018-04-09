from django.db import models


from authentication.models import User

class Week(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    week_num = models.IntegerField(null=True)

    PAST_WEEK_BEFORE_SIGNUP = 'PWBS'
    PAST_WEEK_NO_OBJ = 'PWNO'
    PAST_WEEK_MISSED_OBJ = 'PWMO'
    PAST_WEEK_OBJ_ACHIEVED = 'PWOA'

    CURRENT_WEEK_NO_OBJ = 'CWNO'
    CURRENT_WEEK_WITH_OBJ = 'CWWO'
    CURRENT_WEEK_OBJ_ACHIEVED = 'CWOA'

    FUTURE_WEEK_NO_OBJ = 'FWNO'
    FUTURE_WEEK_WITH_OBJ = 'FWWO'

    DEATH = 'DEATH'

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
        (DEATH, 'This is were you die!'),
    )

    week_status = models.CharField(
        max_length=5,
        choices=WEEK_STATUSES,
        blank=True,
    )
    def save(self, *args, **kwargs):
        objectives = self.objective_set.all()
        print(len(objectives))
        has_objectives = True if len(objectives) > 0 else False
        all_achieved = False

        for objective in objectives:
            all_achieved = objective.objective_achieved

        print("All achieved{}".format(all_achieved))
        if self.week_status == Week.CURRENT_WEEK_NO_OBJ:
            if has_objectives:
                print("has objectives")
                self.week_status = Week.CURRENT_WEEK_WITH_OBJ

        if self.week_status == Week.CURRENT_WEEK_WITH_OBJ:
            print(Week.CURRENT_WEEK_WITH_OBJ)
            if all_achieved:
                print("SETTING TO CWOA!!")
                self.week_status = Week.CURRENT_WEEK_OBJ_ACHIEVED

        super(Week, self).save(*args, **kwargs)

class Objective(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    objective_achieved = models.BooleanField(default=False)
