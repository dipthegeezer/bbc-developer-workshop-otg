Feature: Online availability window
  Scenario: A page to display the online availability window
      Given a user visits the winter olympics catchup page
      When the page is rendered
      Then I should see a list of programme titles
      And  subtitles
      And  the online availability window
