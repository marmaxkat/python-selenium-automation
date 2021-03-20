# Created by inna at 2/14/21
Feature:Test for dress selection
  # Enter feature description here

  Scenario: User can select color
    Given Open Amazon Dress B07K16R9V3 page
    Then Verify user can click through color


  Scenario: Size tooliip is shown upon hovering over Add to cart button
    Given Open Amazon product B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown