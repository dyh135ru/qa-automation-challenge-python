@saucedemo @checkout @regression
Feature: Checkout Process
  As a user with items in the cart
  I want to complete the checkout process
  To receive my order

  Background:
    Given the user has items in the shopping cart

  @smoke
  Scenario: Complete a successful purchase flow
    When the user proceeds to checkout
    And fills the information with "John", "Doe", "12345"
    And confirms the order summary
    Then the order should be completed with message "Thank you for your order!"

  @negative
  Scenario: Validate required fields in checkout information
    When the user proceeds to checkout
    And clicks continue without entering information
    Then an error message "Error: First Name is required" should be displayed
