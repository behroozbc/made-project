# Colder Days, Cheaper Tickets?

## Project Description

This project looks into the cost of flight tickets in North America, and the changes are related to temperature. By inspecting to flight and weather data from 2018, I aim to determine if there's a relation between temperature and ticket prices.

**Summary:**

- **Data Sources**: 

  - 2018 Airplane Flights from Kaggle - Contains flight price, distance, and quarter of the year.

  - Average Day Weather for 2018 from Kaggle - Provides daily average dew point temperatures of 2018.

- **Pipline**: 

	- Mapped weather data to flight data by quarter.

	- Develpoed by Python.

	- Use kaggle and panda packages.

	- Save the data in CSV file.

	- Calculated average temperature and price per mile for each quarter.

- **Analysis Method**: 

  - Used Pearson Correlation Coefficient (PCC) to assess the correlation between temperature and ticket price.

- **Findings**: 

  - The PCC was calculated to be -0.65, indicating an inverse relationship where ticket prices increase as temperatures decrease. Therefore, "Colder days, cheaper tickets?" is answered with a **No**.

- **Reasons for Price Increase in Winter**: 

  - Winter holidays increase travel demand.

  - Tourism patterns shift towards warmer destinations or winter sports areas.

  - Increased operational costs due to weather challenges like de-icing.



- **Limitations**: 

  - Does not account for public or school holidays.

  - Monthly price variations not considered because of needs a more accurate flights dataset.



- **Future Work**: 

  - Find a dataset to include monthly data for more precise analysis.

  - Consider public and school holidays as influencing factors.

  - Investigate operational cost impacts on ticket pricing.
