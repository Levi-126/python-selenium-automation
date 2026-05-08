# Created by levi126 at 5/7/26
Feature: Navigation Of Logged Out User

  Scenario: Logged Out User Can Reach Sign In Page
    Given Open Target Webpage
    When Select Your Account
    And Choose To Sign In
    Then Verify Log In Is Possible
