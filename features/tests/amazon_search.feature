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


#  Scenario: User can search for a Dress
#    Given Open Amazon page
#    When Input Dress into Amazon search field
#    And Click on Amazon search icon
#    Then Product results for Dress are shown
#    And Page URL has Dress in it