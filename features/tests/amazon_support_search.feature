# Created by inna at 2/6/21
Feature: Amazon support search
  # Enter feature description here

   Scenario Outline: User searches for Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input <search_text> into search field
    And Click Enter
    Then Verify that <result_text> text is present
     Examples:
    |search_text  | result_text            |
    |Cancel order |"Cancel Items or Orders"|