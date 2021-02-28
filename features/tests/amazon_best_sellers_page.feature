# Created by inna at 2/10/21
Feature: Amazon Best Sellers Page has 5 links
  # Enter feature description here

#  Scenario:
#    Given Open Amazon Best Sellers page
#    Then Verify there are 5 links



  Scenario:
    Given Open Amazon page
    When Click on Best Sellers link
    And Store BS window
    Then  Clicks on each top link and verify that new page opens
