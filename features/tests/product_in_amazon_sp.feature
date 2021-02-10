# Created by inna at 2/6/21
Feature: Product in Shoping Cart
  # Enter feature description here

  Scenario: Verify that Product is in Shopping Cart
    Given Open Amazon page
    When Input watch into Amazon search field
    And Click on first product
    And Select color
    And Click on Add to cart button
    Then Verify cart has 1 item