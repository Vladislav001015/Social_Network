from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from network_app import serializer
from network_app.models import Post, Like, DisLike
from network_app.serializer import UsersSerializer

from .permissions import IsOwnerOrReadOnly


class UserRegistationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializer.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UsersSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializers


class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )


class PostCreateView(generics.CreateAPIView):
    serializer_class = serializer.PostSerializers
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializers


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializer.PostSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializer.LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DisLikeCreateView(generics.ListCreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = serializer.DisLikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
