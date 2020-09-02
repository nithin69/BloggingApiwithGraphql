import graphene
from blog.graphql.nodes import PostNode, CommentNode
from blog.models import Post, Comment
from datetime import datetime


class CreatePost(graphene.Mutation):

    post = graphene.Field(PostNode)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(required=True)

    def mutate(self, *args, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        author = kwargs.get('author')

        post = Post.objects.create(
            title=title,
            description=description,
            author=author,
            created_at=datetime.now()
        )

        post.save()

        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):

    post = graphene.Field(PostNode)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=False)
        description = graphene.String(required=False)
        author = graphene.String(required=False)
        created_at = graphene.DateTime(required=False)

    def mutate(self, *args, **kwargs):
        post_id = kwargs.get('id')
        title = kwargs.get('title')
        description = kwargs.get('description')
        author = kwargs.get('author')
        created_at = kwargs.get('created_at')

        post = Post.objects.get(pk=post_id)

        if title is not None:
            post.title = title

        if description is not None:
            post.description = description

        if author is not None:
            post.author = author

        if created_at is not None:
            post.created_at = publish_date

        post.save()

        return CreatePost(post=post)


class DeletePost(graphene.Mutation):

    post = graphene.Field(PostNode)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, *args, **kwargs):
        id = kwargs.get('id')
        _ = Post.objects.get(pk=id).delete()

        return _



class CreateComment(graphene.Mutation):

    comment = graphene.Field(CommentNode)

    class Arguments:
        post_id = graphene.ID(required=True)
        author = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, *args, **kwargs):
        post_id = kwargs.get('post_id')
        author = kwargs.get('author')
        content = kwargs.get('content')
        

        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.create(content=content, author=author)

        post.comment = comment
        post.save()

        return CreateComment(comment=comment)


class UpdateComment(graphene.Mutation):

    comment = graphene.Field(CommentNode)

    class Arguments:
        id = graphene.ID(required=True)
        content = graphene.String(required=False)

    def mutate(self, *args, **kwargs):
        comment_id = kwargs.get('id')
        content = kwargs.get('content')

        comment = Comment.objects.get(pk=comment_id)

        if content is not None:
            comment.content = content

        comment.save()

        return CreateComment(comment=comment)



class DeleteComment(graphene.Mutation):

    comment = graphene.Field(CommentNode)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, *args, **kwargs):
        id = kwargs.get('id')
        _ = Comment.objects.get(pk=id).delete()

        return _
