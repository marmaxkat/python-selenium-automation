# Created by inna at 2/18/21
Feature: Amazon Wholefoods page test
  # Enter feature description here

  Scenario: Every product on the Wholefoods page has a text ‘Regular’ and a product name
    Given Open Amazon Wholefoods page
    Then Verify text ‘Regular’ and a product name are displayed