## Flask Application Design

### HTML Files

- **index.html**: The main page of the application.
  - Responsible for displaying trending sneakers and their current prices.
- **details.html**: A page for each sneaker, showing its image, description, and price.

### Routes

- **index**: This route initializes the Flask app and serves the index.html page. It also fetches data on trending sneakers and prices.
- **details/<sneaker_id>**: Accepts a sneaker ID as an argument and serves the details.html page for that specific sneaker. Provides the image, description, and price of the sneaker.

### Implementation Details

1. **index.html**:
   - Includes a list of trending sneakers with their current prices.
   - Has links to the details page for each sneaker.

2. **details.html**:
   - Displays the image of the sneaker.
   - Shows the sneaker's description and price.

3. **index**:
   - Imports the Flask libraries and establishes the Flask app.
   - Fetches data on trending sneakers and their prices from an API.
   - Renders the index.html page, passing the retrieved data.

4. **details/<sneaker_id>**:
   - Accepts a sneaker ID from the URL.
   - Fetches the sneaker's data (image, description, price) from an API.
   - Renders the details.html page, passing the sneaker's data.