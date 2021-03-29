from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):
    """
    This model describes a page on which all comments are made
    """

    name = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    about = models.CharField(
        null=True,
        blank=True,
        max_length=256
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """
        return f"{self.name}"


class AbstractMessage(models.Model):
    """
    This model describes a message sent a user
    """

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )

    message = models.TextField(
        null=True,
        blank=True
    )

    datetime_created = models.DateTimeField(auto_now_add=True)

    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for Abstract Message
        """
        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """
        return f"{self.message} by {self.user.username}"


class ParentMessage(AbstractMessage):
    """
    This model describes the parent message sent by any user
    """

    page = models.ForeignKey(
        "Page",
        null=True,
        blank=True,
        related_name="messages",
        on_delete=models.CASCADE
    )


class ThreadMessage(AbstractMessage):
    """
    This model describes the thread messages sent by any user
    """

    parent_message = models.ForeignKey(
        "ParentMessage",
        related_name="child_messages",
        on_delete=models.CASCADE
    )
