# Data Visualization Dashboard


## Description

This project is a data visualization dashboard developed using Django, PostgreSQL, and D3.js. It aims to provide interactive visual insights into the provided dataset, focusing on various variables such as intensity, likelihood, relevance, year, country, topics, region, and city.


## Features

- **Interactive Data Visualizations**: Charts and graphs built with D3.js.
- **Dynamic Filtering**: Users can filter data based on end year, topics, sector, region, PEST, source, SWOT, country, and city.
- **API**: A RESTful API to fetch data dynamically from the PostgreSQL database.
- **Responsive Design**: Utilizes Bootstrap for a responsive layout that works on desktop and mobile devices.


## Installation


### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- D3.js
- Node.js and npm (for D3.js and Bootstrap)

### Setup


1. **Clone the repository**

   git clone <https://github.com/sachnaror/Data-Visualization-Dashboard-D3.js>

   cd data_visualization



2. **Install Python dependencies**

   pip install -r requirements.txt


3. **Set up PostgreSQL database**

- Create a new PostgreSQL database.
- Update the `DATABASES` configuration in `settings.py` (line number 86 to 94).


4. **Run migrations**

   python manage.py makemigrations
   python manage.py migrate


5. **Load the dataset**

   - Use the provided script to load the dataset into your database.

    python manage.py loaddata jsdata.json
   

7. **Run the development server**

   python manage.py runserver



Visit `http://localhost:8000` in your browser to view the dashboard.



## Usage

- Navigate through the dashboard to view different data visualizations.
- Use the filter options provided to refine the visualizations based on specific criteria.
- API endpoints can be accessed for custom data retrieval.



## API Reference

Document your API endpoints here, with examples of usage (i will add this here shortly).



## Contact

For any queries, you can reach out to <schnaror@gmail.com> or WhatsApp : 0919560330483
