from django.contrib import admin

from . import models


@admin.register(models.PublicKey)
class PublicKeyAdmin(admin.ModelAdmin):  # type:ignore[type-arg]
    list_display = ["user", "comment", "last_used_on"]
    fields = ["user", "comment", "key", "last_used_on"]
    raw_id_fields = ["user"]


@admin.register(models.JWKSEndpointTrust)
class JWKSEndpointTrustAdmin(admin.ModelAdmin):  # type:ignore[type-arg]
    list_display = ["user", "jwks_url", "last_used_on"]
    fields = ["user", "jwks_url", "last_used_on"]
    raw_id_fields = ["user"]
