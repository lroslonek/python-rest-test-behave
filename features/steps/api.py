from behave import *

from assertions.posts_asertions import PostsAssertions
from factory.posts_factory import PostFactory
from service.todos_service import PostService

use_step_matcher("re")


@when("get all posts")
def step_impl(context):
    context.response = PostService.get_all_posts()


@then("all the posts are returned correctly")
def step_impl(context):
    assert PostsAssertions.is_get_all_posts_response_ok(context.response)


@when("get single post")
def step_impl(context):
    context.response = PostService.get_single_post(1)


@then("single post is returned correctly")
def step_impl(context):
    assert PostsAssertions.is_single_post_response_ok(context.response)


@given("new post is prepared")
def step_impl(context):
    context.post = PostFactory.get_new_post()


@when("add new post")
def step_impl(context):
    context.response = PostService.add_new_post(context.post)


@then("new post is added correctly")
def step_impl(context):
    assert PostsAssertions.is_add_new_post_response_ok(context.post, context.response)


@when("update existing post")
def step_impl(context):
    context.response = PostService.update_existing_post(post_id=1, post=context.post)


@then("new post is updated correctly")
def step_impl(context):
    assert PostsAssertions.is_update_post_response_ok(context.post, context.response)


@when("delete single post")
def step_impl(context):
    context.response = PostService.delete_single_post(1)


@then("post is deleted correctly")
def step_impl(context):
    assert PostsAssertions.is_delete_post_response_ok(context.response)
