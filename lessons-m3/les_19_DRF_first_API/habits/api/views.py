from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from habits.models import Habit
from .serializers import HabitSerializer


class HabitListCreateApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        if request.user.is_authenticated:
            queryset = Habit.objects.filter(user=request.user).order_by('-created_at')
        else:
            queryset = Habit.objects.filter(is_public=True).order_by('-created_at')

        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HabitSerializer(data=request.data)

        if not equest.user.is_authenticated:
            return Response(
                {'detail': 'Необходимо залогиниться'},
                status=status.HTTP_401_UNAUTHORIZED

            )

        if serializer.is_valid():
            habit = serializer.save(user=request.user)
            return Response(HabitSerializer(habit).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)