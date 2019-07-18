import numpy as np
from .models import *
from django.db.models import Avg


def inner_product(sample1, sample2):
    sample1 = np.array(list(sample1.values()), dtype=np.float)
    sample2 = np.array(list(sample2.values()), dtype=np.float)

    return np.dot(sample1, sample2)


def recommend(username, category):
    userprofile = UserProfile.objects.get(user__username=username)
    preference = Preference.objects.filter(user=userprofile, category=category).values()[0]
    teas = Tea.objects.filter(category=category).all().values()
    pref_id = preference.pop('id')
    user_id = preference.pop('user_id')
    category = preference.pop('category')

    def sort_tea(tea):
        tea_id = tea.pop('id')
        tea_name = tea.pop('tea_name')
        tea.pop('category')
        result = inner_product(preference, tea)

        tea['id'] = tea_id
        tea['tea_name'] = tea_name
        tea['category'] = category

        return result

    return sorted(teas, key=sort_tea, reverse=True)


def create_preference(username, category):
    userprofile = UserProfile.objects.get(user__username=username)
    eval_average = Evaluation.objects.filter(user=userprofile, category=category, like=True).all() \
        .aggregate(
        strong_average=Avg('strong'),
        long_average=Avg('long'),
        heavy_average=Avg('heavy'),
        complex_average=Avg('complex'),
        gorgeous_average=Avg('gorgeous'),
        sweet_average=Avg('sweet'),
        bitter_average=Avg('bitter'),
        sour_average=Avg('sour'),
        umami_average=Avg('umami'),
        aftertaste_average=Avg('aftertaste'),
        roundness_average=Avg('roundness'),
        smooth_texture_average=Avg('smooth_texture'),
        )
    Preference.objects.create(
        user=userprofile,
        category=category,
        strong=eval_average['strong_average'],
        long=eval_average['long_average'],
        heavy=eval_average['heavy_average'],
        complex=eval_average['complex_average'],
        gorgeous=eval_average['gorgeous_average'],
        sweet=eval_average['sweet_average'],
        bitter=eval_average['bitter_average'],
        sour=eval_average['sour_average'],
        umami=eval_average['umami_average'],
        aftertaste=eval_average['aftertaste_average'],
        roundness=eval_average['roundness_average'],
        smooth_texture=eval_average['smooth_texture_average'],
    )


def update_tea_values(tea_id):
    tea = Tea.objects.get(id=tea_id)
    eval_average = Evaluation.objects.filter(tea=tea, like=True).all() \
        .aggregate(
        strong_average=Avg('strong'),
        long_average=Avg('long'),
        heavy_average=Avg('heavy'),
        complex_average=Avg('complex'),
        gorgeous_average=Avg('gorgeous'),
        sweet_average=Avg('sweet'),
        bitter_average=Avg('bitter'),
        sour_average=Avg('sour'),
        umami_average=Avg('umami'),
        aftertaste_average=Avg('aftertaste'),
        roundness_average=Avg('roundness'),
        smooth_texture_average=Avg('smooth_texture'),
    )
    tea.strong = eval_average['strong_average']
    tea.long = eval_average['long_average']
    tea.heavy = eval_average['heavy_average']
    tea.complex = eval_average['complex_average']
    tea.gorgeous = eval_average['gorgeous_average']
    tea.sweet = eval_average['sweet_average']
    tea.bitter = eval_average['bitter_average']
    tea.sou = eval_average['sour_average']
    tea.umami = eval_average['umami_average']
    tea.aftertaste = eval_average['aftertaste_average']
    tea.roundness = eval_average['roundness_average']
    tea.smooth_texture = eval_average['smooth_texture_average']
    tea.save()
