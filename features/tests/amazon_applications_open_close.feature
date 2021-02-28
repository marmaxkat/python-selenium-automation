# Created by inna at 2/21/21
Feature: User can open amazon applications from Terms of Conditions
  # Enter feature description here


  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to old window
