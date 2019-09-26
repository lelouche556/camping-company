from django.conf import settings
from django.db import models
User = settings.AUTH_USER_MODEL


class UserManager(models.Manager):
    def new_or_get(self, request, totalDays=None, city=None, tripDay=None):
        user_id = request.session.get("user_id", None)
        qs = self.get_queryset().filter(id=user_id)
        if qs.count() == 1:
            new_obj = False
            user_obj = qs.first()
            if request.user.is_authenticated and user_obj.user is None:
                user_obj.user = request.user
                user_obj.save()
        else:
            user_obj = Search.objects.new(totalDays=totalDays, city=city, tripDay=tripDay, user=request.user)
            new_obj = True
            request.session['user_id'] = user_obj.id
        return user_obj, new_obj

    def new(self, totalDays, city, tripDay , user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj, city=city, tripDay=tripDay, totalDays=totalDays)


class Search(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, null=True)
    tripDay = models.DateField(null=True, blank=True)
    totalDays = models.PositiveIntegerField(null=True)
    objects = UserManager()

    def __str__(self):
        return str(self.id)
