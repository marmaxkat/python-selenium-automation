# Created by inna at 2/6/21
Feature: Product in Shoping Cart
  # Enter feature description here

  Scenario: Verify that Product is in Shopping Cart
    Given Open Amazon Product page
    When Press Add to Cart Button
    And Click on the cart icon
    Then Verify that the Product is in Shopping Cart