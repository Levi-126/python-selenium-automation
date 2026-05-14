# Created by levi126 at 5/9/26
Feature: Checking Item Cart Acknowledgement

  Scenario: Make Sure Items Are Added to Cart
     Given Open Target Webpage
     When Search for Bamboo
     Then Add Item to Cart
     Then Confirm Add Item to Cart
     Then Select The View Cart Option
     Then Verify Item In Cart Is 1



  #Create a test case to add any Target’s product into the cart,
  #and make sure it’s there (check that your cart has individual
  # cart items OR the total price, up to you!)
