# Created by levi126 at 5/7/26
Feature: Validate Empty Search From Target

  Scenario: Too Broke To Buy Anything From Target
    Given Open Target Webpage
    When Select The Cart Icon
    Then Verify The Cart Is Empty