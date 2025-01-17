import openai
import json

# Set your API key and the base URL for Perplexity
openai.api_key = "INSERT_API_KEY_HERE(PERPLEXITY API)"
openai.api_base = "https://api.perplexity.ai"

def search_products(query):
    """
    Use Perplexity to search for real product data on Amazon and eBay.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI with internet access capable of searching Amazon and eBay. "
                "Do not fabricate data. If uncertain, say 'N/A'. "
                "Use the structure:\n"
                "{\n"
                "  \"products\": [\n"
                "    {\n"
                "      \"Title\": \"...\",\n"
                "      \"Price\": \"...\",\n"
                "      \"Rating\": \"...\",\n"
                "      \"Description\": \"...\",\n"
                "      \"Prime\": \"...\",\n"
                "      \"Image_Url\": \"...\",\n"
                "      \"Site\": \"Amazon\" or \"Ebay\"\n"
                "    }\n"
                "  ]\n"
                "}"
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
    Parse the JSON string from the LLM's 'content' field.
    Return a list of product dictionaries or an empty list on failure.
    """
    if not response or "choices" not in response:
        return []

    content = response["choices"][0].get("message", {}).get("content", "")
    if not content:
        return []

    try:
        data = json.loads(content)
        if isinstance(data, dict) and "products" in data:
            return data["Products"]
        else:
            print("Top 5 results have been displayed")
            return []
    except json.JSONDecodeError:
        print("Here are your results:")
        print(content)
        return []

def main():
    print("\033[1;31m   ██████╗██╗        █████╗ ████████╗███████╗")
    print("   ██╔════╝██║       ██╔══██╗╚══██╔══╝██╔════╝")
    print("   ██║     ██║       ███████║   ██║   ███████╗")
    print("   ██║     ██║       ██╔══██║   ██║   ╚════██║")
    print("   ██████╗ ███████╗  ██║  ██║   ██║   ███████║")
    print("   ╚═════╝ ╚══════╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝\033[0m")
    print("\033[1;34mC      L       A       T       S       E       A       R       C       H       (Version 1.00)\033[0m")

    query = input("Enter an Amazon or Ebay product name: ")
    raw_response = search_products(query)
    
    if not raw_response:
        print("No response from Perplexity.")
        return
    
    products = parse_response(raw_response)
    if not products:
        print("Thank you for using ClatSearch.")
        return
    
    print(f"\n=== Found {len(products)} Products ===\n")
    for i, product in enumerate(products, start=1):
        title = product.get("Title", "N/A")
        price = product.get("Price", "N/A")
        rating = product.get("Rating", "N/A")
        description = product.get("Description", "N/A")
        prime = product.get("Prime", "N/A")
        image_url = product.get("Image_Url", "N/A")
        site = product.get("Site", "N/A")

        print(f"{i}. Title: {title}")
        print(f"   Price: {price}")
        print(f"   Description: {description}")
        print(f"   Rating: {rating}")
        print(f"   Prime Available (Amazon only): {prime}")
        print(f"   Image URL: {image_url}")
        print(f"   Site: {site}\n")

if __name__ == '__main__':
    main()
    input("\nPress Enter to close...")