# Created by inna at 2/14/21
Feature: Amazon Sign In tests
  # Enter feature description here

  Scenario: Sign In page can be opened from popup
    Given Open Amazon page
    When  Click Sign In from popup
    Then Verify Sign in page opens



  Scenario: Amazon users can see Sign In button
    Given Open Amazon page
    Then Verify Sign in is clickable
    When  Wait for 5 sec
    Then Verify Sign in is clickable
    Then Verify Sign in is disappears