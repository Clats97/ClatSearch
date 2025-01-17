# ClatSearch

**Information for the ClatSearch Tool**

**Overview**

The ClatSearch tool enables users to search for real-time product data from Amazon and eBay using the Perplexity AI API. By entering a product query, users receive structured product details such as title, price, rating, description, availability of Prime (Amazon), and an image URL. The script is particularly useful for comparative shopping, market analysis, and product research.
________________________________________

**Features**

•	Cross-Platform Search: Fetches product data from Amazon and eBay.
•	Structured Output: Presents data in an organized format for easy interpretation.
•	Error Handling: Manages API errors gracefully and informs users when results cannot be retrieved.
•	Interactive Interface: Users can input queries and receive multiple results within the terminal.
•	Detailed Product Information: Includes details such as price, rating, description, and availability.
________________________________________

**Why It’s Useful**

•	E-commerce Research: Facilitates comparative shopping by fetching results from multiple platforms.
•	Market Analysis: Useful for identifying trends, pricing benchmarks, and product availability.
•	Efficiency: Automates manually browsing Amazon and eBay for product information.
•	Integration: Provides structured data that can be easily parsed for further processing in other applications.
________________________________________

**How to Set Up ClatSearch**

**Prerequisites**

Python Installation: Ensure Python 3.8 or higher is installed on your system.
Required Libraries: Install the following Python libraries: 
•	Openai
•	json Use the command: pip install openai.
•	

**API Key Setup**

1.	Obtain an API key for the Perplexity AI service.
2.	Replace the placeholder API key in the script with your own. 
3.	openai.api_key = "your_api_key_here"
4.	

**Running the Script**

1.	Save the script.
2.	Open a terminal or command prompt.
3.	Run the script using: python clatsearch.py
4.	Alternatively, you can just click on the file and open it, or open it in Visual Studio Code
5.	Follow the prompts to enter a product name or description. The script will fetch and display the results in the terminal.
________________________________________

**Script Details**

Key Functions
search_products(query): 
•	Sends a query to the Perplexity API.
•	Fetches product data from Amazon and eBay.
•	parse_response(response): 
o	Parses the API response.
o	Extracts product details and handles JSON decoding errors.
•	main(): 
o	Handles user interaction.
o	Calls the necessary functions to search and display results.
________________________________________

**Limitations**

1.	API Dependency: Requires a valid API key and connectivity to Perplexity AI.
2.	Error Handling: While robust, occasional parsing errors may occur if the API response format changes.
3.	Platform Scope: Currently limited to Amazon and eBay searches.
________________________________________

**Future Enhancements**

•	Add support for additional e-commerce platforms (e.g. Walmart, Best Buy).
•	Implement a graphical user interface (GUI) for ease of use.
•	Export results to CSV or Excel for offline analysis.
•	Integrate with additional APIs for more comprehensive product data.
________________________________________

**Example Output**

Input:

Enter an Amazon or Ebay product name: wireless earbuds

Output:

=== Found 2 Products ===
1. Title: Wireless Earbuds with Noise Cancellation
   Price: $49.99
   Description: High-quality wireless earbuds with active noise cancellation.
   Rating: 4.5/5
   Prime Available (Amazon only): Yes
   Image URL: https://example.com/image1.jpg
   Site: Amazon
2. Title: Bluetooth Earbuds 2023
   Price: $29.99
   Description: Budget-friendly Bluetooth earbuds with long battery life.
   Rating: 4.0/5
   Prime Available (Amazon only): No
   Image URL: https://example.com/image2.jpg
   Site: Ebay

Thank you for using ClatSearch.
