@saucedemo @login
Feature: SauceDemo Authentication
  As a user
  I want to authenticate into the platform
  To manage my shopping cart

  Background:
    Given the user is on the SauceDemo login page

  @smoke @regression
  Scenario: Successful login with valid credentials
    When the user enters username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the inventory page
    And the product title "Products" should be visible

  @regression
  Scenario Outline: Failed login with invalid credentials
    When the user enters username "<username>" and password "<password>"
    Then an error message "<error_message>" should be displayed

    Examples:

      | username        | password       | error_message                                               |
      | locked_out_user | secret_sauce   | Epic sadface: Sorry, this user has been locked out.          |
      | wrong_user      | secret_sauce   | Epic sadface: Username and password do not match any user   |
      | standard_user   | wrong_password | Epic sadface: Username and password do not match any user   |
