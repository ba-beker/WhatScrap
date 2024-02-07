# WhatScrap

## Introduction
This project is a Python script designed to interact with a specific API for extracting information from an online platform. The script utilizes the `pywhatkit` and `numpy` libraries for additional functionality.

## Getting Started
To use this script, follow these steps:

1. Install the required libraries:
    ```bash
    pip install pywhatkit numpy requests
    ```

2. Replace the placeholder `"LINK"` in the script with the actual API endpoint you want to query.

3. Ensure that you have the necessary authorization details for the API in the `headers` dictionary.

4. Save the script and execute it using a Python interpreter.

## Script Overview
The script performs the following actions:

1. Sends a POST request to the specified API endpoint with predefined headers and payload.
2. Extracts relevant information from the API response, focusing on store announcements.
3. Identifies the store with the maximum number of announcements and retrieves additional details.
4. Uses the `pywhatkit` library to send WhatsApp messages to the store's contact number.

## Usage
The script is designed to be used as an automated tool for interacting with the specified API. It can be scheduled to run at specific intervals to keep track of stores and send messages accordingly.

## Dependencies
- `pywhatkit`: Used for sending WhatsApp messages.
- `numpy`: Used for array operations and data manipulation.
- `requests`: Used for making HTTP requests to the API.

## Important Notes
- Ensure that you have the necessary permissions and comply with the terms of service of the targeted platform before using this script.
- Replace placeholder messages and other content as needed for your specific use case.
- Handle exceptions appropriately to avoid script termination in case of errors.

## Examples:
Here are a few examples of other projects I have worked on:

**Affine Cifer Crypto:** https://github.com/ba-beker/Affine_Cifer_Crypto

**Push Swap :** https://github.com/ba-beker/push_swap

**so_long:** https://github.com/ba-beker/so_long

Feel free to explore these projects to get a better understanding of my range of skills and coding style.

If you have any questions or would like to discuss this project further, please feel free to contact me. Thank you for taking the time to review my work!
