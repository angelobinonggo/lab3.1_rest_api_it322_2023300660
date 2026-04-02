import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

logger = logging.getLogger(__name__)


class StudentViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that provides CRUD operations for Student records.

    list:   GET  /api/v1/students/          - Retrieve all students (paginated)
    create: POST /api/v1/students/          - Create a new student
    retrieve: GET /api/v1/students/{id}/    - Retrieve a single student
    update: PUT  /api/v1/students/{id}/     - Fully update a student
    partial_update: PATCH /api/v1/students/{id}/ - Partially update a student
    destroy: DELETE /api/v1/students/{id}/  - Delete a student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        logger.info(f"Student list accessed by user: {request.user}")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating new student record by user: {request.user}")
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"Student record {kwargs.get('pk')} retrieved by user: {request.user}")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        logger.info(f"Updating student record {kwargs.get('pk')} by user: {request.user}")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        logger.warning(f"Deleting student record {kwargs.get('pk')} by user: {request.user}")
        return super().destroy(request, *args, **kwargs)
