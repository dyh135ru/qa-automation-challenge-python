@regression @dynamic
Feature: Dynamic Loading

  Scenario: Wait for dynamic content to load
    Given the user is on the dynamic loading page
    When the user clicks the start button
    Then the text "Hello World!" should appear after loading

