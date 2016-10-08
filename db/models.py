import sys
try:
    from django.db import models
except Exception:
    print("Django Not Found,please install it")
    sys.exit()


# Sample  model
class User(models.Model):
    name = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name

    __repr__ = __str__