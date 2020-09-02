import graphene
from blog.graphql import nodes , mutations
from blog.models import Post, Comment


class Query(graphene.ObjectType):

    posts = graphene.List(nodes.PostNode)
    post = graphene.Field(nodes.PostNode, id=graphene.ID())

    comments = graphene.List(nodes.CommentNode)


    def resolve_posts(self, *args, **kwargs):
        return Post.objects.all()

    def resolve_post(self, *args, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Post.objects.get(pk=id)


    def resolve_comments(self, *args, **kwargs):
        return Comment.objects.all()


class Mutation(graphene.ObjectType):
    # Post Crud Operation
    create_post = mutations.CreatePost.Field()
    update_post = mutations.UpdatePost.Field()
    delete_post = mutations.DeletePost.Field()
    # Comment Crud Operation
    create_comment = mutations.CreateComment.Field()
    update_comment = mutations.UpdateComment.Field()
    delete_comment = mutations.DeleteComment.Field()
