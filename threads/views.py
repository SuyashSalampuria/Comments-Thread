from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Page, ThreadMessage, ParentMessage
from .serializers import PageSerializer, PageDetailSerializer, ThreadMessageSerializer, ParentMessageSerializer


class PageViewSet(viewsets.ModelViewSet):
    """
    View to get the list of all the pages
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_serializer_class(self):
        """
        Use PageDetailSerializer for detail view and PageSerializer
        for other actions
        """
        if(self.action == 'retrieve'):
            return PageDetailSerializer
        return PageSerializer


class ParentMessageViewSet(viewsets.ModelViewSet):
    """
    View to get the list of all parent Message
    """
    queryset = ParentMessage.objects.all()
    serializer_class = ParentMessageSerializer


class ThreadMessageViewSet(viewsets.ModelViewSet):
    """
    View to get the list of all thread Message
    """
    queryset = ThreadMessage.objects.all()
    serializer_class = ThreadMessageSerializer
