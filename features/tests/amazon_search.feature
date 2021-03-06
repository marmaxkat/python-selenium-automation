# Created by inna at 1/24/21
Feature: Amazon Search Test
  # Enter feature description here

  Scenario Outline: User can search for a Watches
    Given Open Amazon
    When Input <search_query> into Amazon search field
    And Click on Amazon search icon
    Then Product results for <result> are shown successfully
    And Page URL has <search_query> in it
    Examples:
    |search_query| result  |
    |Watches     |"Watches"|
    |Dress       |"Dress"  |


  Scenario: User can add product to the cart
    Given Open Amazon page
    When Input coffee mug into Amazon search field
    And Click on first product
    And Click on Add to cart button
    Then Verify cart has 1 item

  Scenario: User can add product to the cart
    Given Open Amazon page
     And Click on first product
    And Select shoes size
    And Click on Add to cart button
    Then Verify cart has 1 item


  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <departments>
    And Seasch for <search_query>
    Then Verify <departments> department is selected
    Examples:
    |departments|search_query|
    |stripbooks |Faust       |
    |garden     |mug         |
