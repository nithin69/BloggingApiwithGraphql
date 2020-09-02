import graphene
# from blog.schema import Query, Mutation
# OR
import blog.graphql.schema


class Query(blog.graphql.schema.Query, graphene.ObjectType):
    pass


class Mutation(blog.graphql.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)