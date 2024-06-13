from django.urls import get_resolver

def list_urls():
    # Get the URL resolver from Django
    resolver = get_resolver()
    
    # Initialize an empty list to store the URLs
    urls = []
    
    # Loop through each URL pattern in the resolver's URL patterns
    for url_pattern in resolver.url_patterns:
        # Convert the URL pattern to a string and append it to the URLs list
        urls.append(str(url_pattern.pattern))
    
    # Return the list of URLs
    return urls