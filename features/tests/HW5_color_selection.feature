# Created by inna at 2/18/21
Feature: Test for Jean selection
  # Enter feature description here

  Scenario Outline: User can select color
    Given Open Amazon <url_query> page
    Then Verify user can click through <color_list> colors
    Examples:
    |url_query                                    |color_list                                |
    |https://www.amazon.com/gp/product/B07BJKRR25/|Black,Blue Overdyed,Dark Vintage,Dark Wash,Indigo Wash,Light Vintage,Light Wash,Medium Vintage,Medium Wash,Rinse,Rinsed Vintage,Vintage Light Wash,Washed Black|
    |https://www.amazon.com/gp/product/B07K16R9V3/|Emerald,Ivory,Navy                        |