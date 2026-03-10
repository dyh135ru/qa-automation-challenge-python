@regression
Feature: Dropdown Selection

  Scenario: Select an option from the dropdown menu
    Given the user is on the dropdown page
    When the user selects the option "Option 1"
    Then the selected value should be "1"
