from django.db import models

# Custom Field Definitions
class MySQLBitBooleanField(models.BooleanField):
    """
    Custom field definition to cater for MySQL bit field
    Adapted from https://github.com/adamchainz/django-mysql
    Note:
    - Wanted to use django-mysql's Bit1BooleanField but ran into error even though none was knowingly defined: 
      MySQLdb._exceptions.OperationalError: (1193, "Unknown system variable 'innodb_strict_mode'")
    """
    def db_type(self, connection):
        return "bit(1)"

    def from_db_value(self, value, expression, connection):
        if isinstance(value, bytes):
            value = value == b"\x01"
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        else:
            return 1 if value else 0

class TextBooleanField(models.BooleanField):
    """
    Custom field created to model a boolean type field that has been formatted as "TEXT"
    in the CMS MySQL database
    Used by: cmsinv.InventoryItem
    """
    def db_type(self, connection):
        return "boolean like text"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value 
        elif value is "1":
            return True
        else:
            return False
        
    def get_prep_value(self, value):
        if value is None:
            return value
        else:
            return 1 if value else 0

class AuditLog(models.Model):
    """
    Maps to CMS table: audit_log
    """
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField(default=0)
    actor = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    event_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    new_value = models.TextField(blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    persisted_object_id = models.CharField(max_length=255, blank=True, null=True)
    persisted_object_version = models.CharField(max_length=255, blank=True, null=True)
    property_name = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'
        app_label = 'cmssys'
        ordering = ['-last_updated']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('drugdb.views.details', args=[str(self.id)])

    def __str__(self):
        return f"{self.date_created} [{self.actor}] {self.event_name} {self.class_name}: {self.property_name} - {self.old_value} => {self.new_value}"
  
class CmsUser(models.Model):
    """
    Maps to CMS table: user
    """
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField(default=0)
    active = models.BooleanField(default=True)
    cname = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    medical_council_reg_no = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    tel = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.PROTECT, db_column='user_profile_id')
    username = models.CharField(unique=True, max_length=255)
    ehr_uid = models.CharField(max_length=255, blank=True, null=True)
    priority = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        app_label = 'cmssys'
        ordering = ['id']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cmssys.views.details', args=[str(self.id)])

    def __str__(self):
        return f"{self.id} | {self.username} - {self.name}"

class UserProfile(models.Model):
    """
    Maps to CMS table user_profile
    """
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'user_profile'
        app_label = 'cmssys'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('cmssys.views.details', args=[str(self.id)])

    def __str__(self):
        return f"{self.id} | ver.{self.version}"