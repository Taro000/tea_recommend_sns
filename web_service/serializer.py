from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'user',
            'profile_name',
            'icon',
            'header',
            'introduction',
            'birthday',
            'gender',
        )


class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = (
            'id',
            'tea_name',
            'category',
            'strong',
            'long',
            'heavy',
            'complex',
            'gorgeous',
            'sweet',
            'bitter',
            'sour',
            'umami',
            'aftertaste',
            'roundness',
            'smooth_texture',
        )


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = (
            'id',
            'user',
            'tea',
            'category',
            'strong',
            'long',
            'heavy',
            'complex',
            'gorgeous',
            'sweet',
            'bitter',
            'sour',
            'umami',
            'aftertaste',
            'roundness',
            'smooth_texture',
        )


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = (
            'id',
            'user',
            'category',
            'strong',
            'long',
            'heavy',
            'complex',
            'gorgeous',
            'sweet',
            'bitter',
            'sour',
            'umami',
            'aftertaste',
            'roundness',
            'smooth_texture',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'evaluation',
            'text',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'date_posted',
        )
