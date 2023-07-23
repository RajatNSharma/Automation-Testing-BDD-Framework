Feature: OrangeHRM Login

  Background: common steps
    Given Launch browser
    When Open application
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search User
    When navigate to advanced search page
    Then search page should display
