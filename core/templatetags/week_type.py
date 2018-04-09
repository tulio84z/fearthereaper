from django import template

from core.models import Week

register = template.Library()

@register.filter
def weekbtn(value):

    options_colors = {
        Week.PAST_WEEK_BEFORE_SIGNUP :"btn ",
        Week.PAST_WEEK_NO_OBJ :"btn btn-danger",
        Week.PAST_WEEK_MISSED_OBJ :"btn btn-danger",
        Week.PAST_WEEK_OBJ_ACHIEVED :"btn btn-success",

        Week.CURRENT_WEEK_NO_OBJ :"btn btn-warning",
        Week.CURRENT_WEEK_WITH_OBJ :"btn btn-info",
        Week.CURRENT_WEEK_OBJ_ACHIEVED :"btn btn-success",

        Week.FUTURE_WEEK_NO_OBJ :"btn btn-default",
        Week.FUTURE_WEEK_WITH_OBJ :"btn btn-primary",

        Week.DEATH :"btn ftr-blk-bnt",
    }

    return options_colors[value]
