# Created by inna at 2/14/21
Feature: Amazon Sign In tests
  # Enter feature description here

  Scenario: Sign In page can be opened from popup
    Given Open Amazon page
    When  Click Sign In from popup
    Then Verify Sign in page opens