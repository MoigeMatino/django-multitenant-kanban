from django.contrib.auth.models import AbstractUser
from tenant_users.tenants.models import TenantBase, UserProfile
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from core.models import TimeStampedModel


class User(UserProfile):
    pass


class Tenant(TenantBase, TimeStampedModel):
    name = models.CharField(max_length=100)


class Domain(DomainMixin, TimeStampedModel):
    pass
