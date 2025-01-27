import openai
import json

openai.api_key = "INSERT PERPLEXITY API KEY HERE"
openai.api_base = "https://api.perplexity.ai"

def search_products(query):
    """
    Use Perplexity to search for real product data on Amazon and eBay.
    """
    messages = [
        {
            "role": "system",
            "content": (
            "You are a helpful AI assistant with access to real-time product information from Amazon and eBay." 
            "When searching for products, show at least 5 results from each platform, with each result showing:" 
            "Title (full product name), Price (current and original if discounted), Rating (x/5 with review count)," 
            "Description, Shipping (delivery options and estimated time), Seller (name and reliability score)," 
            "Platform (website and domain), Stock Status (quantity/availability), whether or not it is a prime product," 
            "and its Condition (New/Used/Refurbished). Sort results by relevance and verified reviews by default, but accept" 
            "custom sorting by price, rating, or review count. Mark any unavailable information as 'N/A' without fabricating data," 
            "and flag any significant information discrepancies. Support filtering by price range," 
            "rating, shipping options, and condition while enabling cross-platform product comparisons. Present all information" 
            "in a clean, human-readable format without JSON structure."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Search for products related to '{query}' on Amazon and eBay. "
                "Return at least 3 items from each site if available."
            ),
        },
    ]

    try:
        response = openai.ChatCompletion.create(
            model="llama-3.1-sonar-huge-128k-online",
            messages=messages
        )
        return response
    except Exception as e:
        print(f"Error calling Perplexity API: {e}")
        return None

def parse_response(response):
    """
    Parse the output from the LLM's 'content' field.
    Return a list of product dictionaries or an empty list on failure.
    """
    if not response or "choices" not in response:
        return []

    content = response["choices"][0].get("message", {}).get("content", "")
    if not content:
        return []

    # Attempt to parse JSON if the response is structured as such.
    # Otherwise, assume it's plain text.
    try:
        data = json.loads(content)
        if isinstance(data, dict) and "products" in data:
            return data["products"]
        else:
            print("Top results have been displayed:\n")
            print(content)
            return []
    except json.JSONDecodeError:
        print("Here are your results:\n")
        print(content)
        return []

def display_products(products):
    """
    Nicely display a list of product dictionaries.
    """
    if not products:
        print("No products to display.\n")
        return

    print(f"\n=== Found {len(products)} Product(s) ===\n")
    for i, product in enumerate(products, start=1):
        title = product.get("Title", "N/A")
        price = product.get("Price", "N/A")
        rating = product.get("Rating", "N/A")
        description = product.get("Description", "N/A")
        prime = product.get("Prime", "N/A")
        site = product.get("Site", "N/A")

        print(f"{i}. Title: {title}")
        print(f"   Price: {price}")
        print(f"   Rating: {rating}")
        print(f"   Description: {description}")
        print(f"   Prime (Amazon only): {prime}")
        print(f"   Site: {site}\n")

def main():
    # ASCII in red
    print("\033[1;31m██████╗██╗      █████╗ ████████╗")
    print("██╔════╝██║     ██╔══██╗╚══██╔══╝")
    print("██║     ██║     ███████║   ██║")
    print("██║     ██║     ██╔══██║   ██║")
    print("╚██████╗███████╗██║  ██║   ██║")
    print(" ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝  ")
    print("███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗")
    print("██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║")
    print("███████╗█████╗  ███████║██████╔╝██║     ███████║")
    print("╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║")
    print("███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║")
    print("╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\033[0m")
    print("\033[1;34mC L A T S E R C H      P R O D U C T      T  O O L "
          "\033[1;31m(Version 1.02)\033[0m")

    while True:
        query = input("\nEnter a product name to search Amazon and Ebay (or 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting ClatSearch.")
            break

        raw_response = search_products(query)
        if not raw_response:
            print("No response from Perplexity or an error occurred.")
            continue

        products = parse_response(raw_response)
        display_products(products)

    input("\nPress Enter to close...")

if __name__ == '__main__':
    main()