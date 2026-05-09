Feature: Verify Product Search Functionality

  Scenario: User can search for a product
    Given Open Target Webpage
    When Search for guitar
    Then Verify search results for guitar shown
