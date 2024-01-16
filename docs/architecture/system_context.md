# ECHO System Overview

## Introduction
This document outlines the ECHO System, focusing on user interactions, system context, and the functionalities of various software components within the system.

## User Interaction
### User
- **Type:** Person
- **Functionality:** Interacts with the ECHO system.

## System Context
### ECHO Backend
- **Type:** Software System
- **Description:** 
  - Contains an Open API.
  - Saves data/metadata and sends the requested information.
  - Forwards metadata requests to the EUSO Data System.

### EUSO Data System
- **Type:** Software System
- **Functionality:** 
  - Retrieves and sends metadata from and to the ECHO Backend.
  - Interacts with the ECHO Backend for data and metadata exchange.

### Web App: ECHO UI
- **Functionality:**
  1. Enables uploading of single or multiple measurements, with or without accompanying data files. Acceptable file formats include images, CSV, XLSX, or NetCDF.
  2. Provides details about updated data by displaying a metadata catalog.
  3. Offers users the option to download selected datasets.

## Internal Interactions
### Metadata Exchange
- **Send Metadata Info:** ECHO Backend sends metadata information to the EUSO Data System.
- **Get Metadata Info:** ECHO Backend retrieves metadata information from the EUSO Data System.

### Data Handling
- **Send a Measurement with a File:** Users can send measurements along with files to the ECHO Backend through the ECHO UI.
- **Get Metadata Information or Requested Dataset:** Users can obtain metadata information or request datasets via the ECHO UI.
