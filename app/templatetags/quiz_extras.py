from django import template

register = template.Library()

def correct_answers_count(selected_options):    
    return selected_options.filter(is_correct=True).count()

register.filter('correct_count' , correct_answers_count)