from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Daily
from .serializers import DailyListSerializer, DailyDetailSerializer


class DailyList(generics.ListAPIView):
    """
    日報の一覧
    isOpen が True になっているものを日付の降順で返す
    """
    queryset = Daily.objects.filter(isOpen=True).order_by('-date')
    serializer_class = DailyListSerializer


class DailyDetail(generics.RetrieveAPIView):
    """
    日報の詳細情報
    """
    queryset = Daily.objects.all()
    serializer_class = DailyDetailSerializer

    def get(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
