@saucedemo @cart @regression
Feature: Shopping Cart Management
  As a logged-in user
  I want to manage my items in the cart
  To prepare my purchase

  Background:
    Given the user is logged into SauceDemo with "standard_user"

  @smoke
  Scenario: Add multiple products to cart
    When the user adds "Sauce Labs Backpack" to the cart
    And the user adds "Sauce Labs Bike Light" to the cart
    Then the cart badge should display "2"

  Scenario: Remove product from inventory page
    Given the user has "Sauce Labs Backpack" in the cart
    When the user removes "Sauce Labs Backpack" from the inventory page
    Then the cart badge should be empty
