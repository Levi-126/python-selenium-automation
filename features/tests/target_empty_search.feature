# Created by levi126 at 5/7/26
Feature: Validate Empty Search From Target

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target Webpage
    When Select The Cart Icon
    Then Verify “Your cart is empty” message is shown

    