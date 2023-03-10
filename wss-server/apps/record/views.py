from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import EventLog, OperationLog
from .pagination import LogPagination
from .serializers import EventLogSerializer, OperationLogSerializer


class DeviceLogAPIView:
	pagination = LogPagination()
	model = None
	serializer = None

	def get(self, request, device_id, *args, **kwargs):
		log_list = self.model.objects.filter(device=device_id)
		result = self.pagination.paginate_queryset(log_list, request)
		log_serializer = self.serializer(result, many=True)
		return self.pagination.get_paginated_response(log_serializer.data)


class EventLogAPI(LoginRequiredMixin, DeviceLogAPIView, APIView):
	model = EventLog
	serializer = EventLogSerializer


class OperationLogAPI(LoginRequiredMixin, DeviceLogAPIView, APIView):
	model = OperationLog
	serializer = OperationLogSerializer
