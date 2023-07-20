# Racool Flight Club

Welcome to the Racool Flight Club project! This Python program is designed to help you find cheap flight deals from your preferred city. It utilizes the Kiwi Tequila API to search for available flights and the Sheety API to manage user data.

## Getting Started

To get started with the Racool Flight Club, follow these simple steps:

1. Make sure you have Python installed on your system.

2. Install the required libraries using the following command:

```
pip install requests
```

3. Create a `.env` file in the same directory as the main Python files (`main.py`, `data_manager.py`, `flight_data.py`, `flight_search.py`, `notification_manager.py`).

4. In the `.env` file, set the necessary environment variables:
   ```
   SHEETYAPI=YOUR_SHEETY_API_KEY
   SEARCHAPI=YOUR_KIWI_TEQUILA_API_KEY
   FLIGHTAPI=YOUR_KIWI_TEQUILA_API_KEY
   USERNAME=YOUR_GMAIL_EMAIL
   PASSWORD=YOUR_GMAIL_PASSWORD
   ```

## How to Use

1. Run the `main.py` file.
2. You will be prompted to enter your first name, last name, and email address to join the Racool Flight Club.
3. The program will automatically search for the cheapest flight deals from the provided city and notify you via email if there are any affordable options.

## Project Structure

- `main.py`: The main script to run the Racool Flight Club program.
- `data_manager.py`: Manages flight and user data using the Sheety API.
- `flight_data.py`: Structures flight data using the Kiwi Tequila API.
- `flight_search.py`: Retrieves airport codes using the Kiwi Tequila API.
- `notification_manager.py`: Handles email notifications using Gmail's SMTP.

## Note

This project relies on the Kiwi Tequila and Sheety APIs. Please ensure you have valid API keys for proper functionality. Also, make sure to enable access for "Less Secure Apps" in your Gmail settings to send notifications via email.

Enjoy finding the best flight deals with Racool Flight Club! 🛫🌍
