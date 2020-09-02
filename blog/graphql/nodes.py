from graphene_django import DjangoObjectType
from blog.models import Post, Comment


# Graphene will automatically map the Post model's fields onto the PostNode.
# This is configured in the PostNode's Meta class (as you can see below)
class PostNode(DjangoObjectType):
    class Meta:
        model = Post

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
