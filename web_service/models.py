from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.utils import timezone


GENDER_CHOICES = (
    ('M', '男性'),
    ('F', '女性'),
    ('O', 'その他'),
)
CATEGORY_CHOICES = (
    ('W', '白茶'),
    ('Y', '黄茶'),
    ('G', '緑茶'),
    ('Bu', '青茶'),
    ('R', '紅茶'),
    ('Bl', '黒茶'),
)


User = get_user_model()


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_name = models.CharField('profile name', max_length=150)
    icon = models.ImageField(upload_to='icon')
    header = models.ImageField(upload_to='header')
    introduction = models.TextField(blank=True, null=True)
    birthday = models.DateField()
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)

    def __str__(self):
        return self.profile_name + '-' + str(self.id)

    def get_profile_name(self):
        return self.profile_name


class Tea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tea_name = models.CharField('tea name', max_length=64)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    strong = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    heavy = models.FloatField(blank=True, null=True)
    complex = models.FloatField(blank=True, null=True)
    gorgeous = models.FloatField(blank=True, null=True)
    sweet = models.FloatField(blank=True, null=True)
    bitter = models.FloatField(blank=True, null=True)
    sour = models.FloatField(blank=True, null=True)
    umami = models.FloatField(blank=True, null=True)
    aftertaste = models.FloatField(blank=True, null=True)
    roundness = models.FloatField(blank=True, null=True)
    smooth_texture = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.tea_name + '-' + str(self.id)


class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='evaluation')
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE, related_name='tea')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    like = models.BooleanField()
    strong = models.FloatField()
    long = models.FloatField()
    heavy = models.FloatField()
    complex = models.FloatField()
    gorgeous = models.FloatField()
    sweet = models.FloatField()
    bitter = models.FloatField()
    sour = models.FloatField()
    umami = models.FloatField()
    aftertaste = models.FloatField()
    roundness = models.FloatField()
    smooth_texture = models.FloatField()

    class Meta:
        unique_together = (
            ('user', 'tea',),
            ('user', 'tea', 'category',),
        )

    def __str__(self):
        return self.user.profile_name + '-' + self.tea.tea_name


class Preference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='preference')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    strong = models.FloatField()
    long = models.FloatField()
    heavy = models.FloatField()
    complex = models.FloatField()
    gorgeous = models.FloatField()
    sweet = models.FloatField()
    bitter = models.FloatField()
    sour = models.FloatField()
    umami = models.FloatField()
    aftertaste = models.FloatField()
    roundness = models.FloatField()
    smooth_texture = models.FloatField()

    class Meta:
        unique_together = (
            'user',
            'category',
        )

    def __str__(self):
        return self.user.profile_name + '-pref-' + str(self.id)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name='post')
    text = models.TextField('text')
    img_1 = models.ImageField('image 1', upload_to='img_1')
    img_2 = models.ImageField('image 2', blank=True, null=True, upload_to='img_2')
    img_3 = models.ImageField('image 3', blank=True, null=True, upload_to='img_3')
    img_4 = models.ImageField('image 4', blank=True, null=True, upload_to='img_4')
    date_posted = models.DateTimeField('date posted', default=timezone.now)

    def __str__(self):
        return self.evaluation.user.profile_name + '-post-' + str(self.id)


class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follow')
    username = models.CharField('username', max_length=150)

    def __str__(self):
        return self.user.profile_name + '-follow-' + str(self.id)


class Follower(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    username = models.CharField('username', max_length=150)

    def __str__(self):
        return self.user.profile_name + '-follower-' + str(self.id)


class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorite')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorite')

    def __str__(self):
        return self.user.profile_name + '-favorite-' + str(self.id)
