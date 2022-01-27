from django.db import models

class App(models.Model):
    """
    An app is installed and other metadata about it.
    """
    def __str__(self):
        return '{}/{}'.format(self.category, self.app_name)

    class Meta:
        """
        Built-in class for overrides.
        """
        db_table = 'app'

    app_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    logo_url = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
