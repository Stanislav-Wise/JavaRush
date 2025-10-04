from rest_framework import mixins, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from habits.models import Habit
from .serializers import HabitSerializer

#
# class HabitListCreateApiView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     GenericAPIView
# ):

class HabitListCreateApiView(ListCreateAPIView):
    """
    GET: список привычек конкретного пользователя
    POST: создание привычки
    """
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Habit.objects.all()

    serializer_class = HabitSerializer

    def get_queryset(self):
        base_qs = super().get_queryset()
        return base_qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    #
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


# class HabitRetrieveUpdateDestroyAPIView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     GenericAPIView
# ):
class HabitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    .../<pk>/
    GET: конкретная привычка
    PUT: обновление привычки
    PATCH: обновление привычки
    DELETE: удаление привычки
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = Habit.objects.all()

    serializer_class = HabitSerializer

    def get_queryset(self):
        base_qs = super().get_queryset()
        return base_qs.filter(user=self.request.user)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, viewsets
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
#
# from habits.models import Habit
# from .serializers import HabitSerializer


# class HabitListCreateApiView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             queryset = Habit.objects.filter(user=request.user).order_by('-created_at')
#         else:
#             queryset = Habit.objects.filter(is_public=True).order_by('-created_at')
#
#         serializer = HabitSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = HabitSerializer(data=request.data)
#
#         if not request.user.is_authenticated:
#             return Response(
#                 {'detail': 'Необходимо залогиниться'},
#                 status=status.HTTP_401_UNAUTHORIZED
#
#             )
#
#         if serializer.is_valid():
#             habit = serializer.save(user=request.user)
#             return Response(HabitSerializer(habit).data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)