# Created by inna at 2/6/21
Feature: Empty Shoping Cart
  # Enter feature description here

  Scenario: Verify that Shopping Cart is empty.
    Given Open Amazon page
    When Click on the cart icon
    Then Verify that Shopping Cart is empty