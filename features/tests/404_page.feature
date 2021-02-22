# Created by inna at 2/21/21
Feature: Test for 404 page
  # Enter feature description here

  Scenario: Amazon 404 page opens blog in another window
    Given Open Amazon Wrond Product page
    When Store original window
    And Click to open blog
    And Switch to the newly opened window
    Then User can close new window and switch back to old window