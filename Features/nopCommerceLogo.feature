# Created by syede at 5/3/2021
Feature: nopCommerce LogoCheck
  Scenario: CheckLogo of nopCommerce LoginPage
    Given Launch Chrome Browser
    When nopCommerce launched
    Then Verify LogoPage of nopCommerce
    And close Browser

