@regression @upload
Feature: File Upload

  Scenario: Successfully upload a test file
    Given the user is on the file upload page
    When the user uploads a test file
    Then the system should display the "File Uploaded!" confirmation message

