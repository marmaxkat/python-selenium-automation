# Created by inna at 1/27/21
Feature: Amazon orders Test
  # Enter feature description here

   Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon main page
    When Verify user logged out
    And Click Orders
    Then Verify Sign in page opened