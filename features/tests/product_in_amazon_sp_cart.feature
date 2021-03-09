# Created by inna at 2/6/21
Feature: Product in Shoping Cart
  # Enter feature description here

  Scenario: User can add product to the cart
    Given Open Amazon
    When Input watch into Amazon search field
    And Click on Amazon search icon
    And Click on first product
    And Select color
    And Click on Add to cart button
    Then Verify cart has 1 item