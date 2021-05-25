# Created by syede at 5/3/2021
Feature: nopCommerce Login
  Scenario: nopCommerce LoginPage Dashboard
    Given Launch the Chrome Browser
    When nopCommerce is launched
    And Enter Username "admin@yourstore.com" and Password "admin" in nopCommerce LoginPage
    And Click on LoginButton
    Then User should be able to successful login into nopCommerce website

  Scenario Outline: nopCommerce LoginPage with Multiple Credentials
    Given Launch the Chrome Browser
    When nopCommerce is launched
    And Enter Username "<username>" and Password "<password>" in nopCommerce LoginPage
    And Click on LoginButton
    Then User should be able to successful login into nopCommerce website
    Examples:
      | username | password |
      | admin@yourstore.com | admin |
      | admin@your.com | admin |
      | admin@yourstore.com | admin123 |
      | admin@.com | admin12 |
