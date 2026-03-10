@saucedemo @responsive @mobile
Feature: Responsive UI Behavior
  As a mobile user
  I want to use the site on a small screen
  To shop on the go

  Scenario: Mobile menu visibility
    Given the user is on the SauceDemo login page with mobile viewport
    When the user logs in as "standard_user"
    Then the side menu button should be visible
    And the inventory layout should adapt to mobile width
