Feature: Post API scenarios

  Scenario: Getting all posts
    When get all posts
    Then all the posts are returned correctly

  Scenario: Getting single post
    When get single post
    Then single post is returned correctly

  Scenario: Adding new post
    Given new post is prepared
    When add new post
    Then new post is added correctly

  Scenario: Updating existing post
    Given new post is prepared
    When update existing post
    Then new post is updated correctly

  Scenario: Deleting existing post
    When delete single post
    Then post is deleted correctly

 