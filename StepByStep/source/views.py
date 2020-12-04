from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from source.models import Problem, Solution, Source, SourceUser
from source.permissions import ReadOnly
from source.serializers import (
    ProblemSerializer,
    SolutionSerializer,
    SourceSerializer,
    SourceUserSerializer,
)


class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [ReadOnly]


class SourceUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SourceUser.objects.all()
    serializer_class = SourceUserSerializer
    permission_classes = [ReadOnly]


class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [ReadOnly]


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [ReadOnly]
