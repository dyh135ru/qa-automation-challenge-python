@smoke @regression
Feature: Form Authentication

  Scenario Outline: Validate authentication with different credentials
    Given the user is on the login page
    When the user enters username "<username>" and password "<password>"
    Then the system should display the message "<expected_message>"

    Examples:

      | username   | password             | expected_message                |
      | tomsmith   | SuperSecretPassword! | You logged into a secure area! |
      | user_wrong | password_wrong       | Your username is invalid!      |
