
# Upwork Jobs Scraper

This project is a Python-based Upwork job scraper that fetches job postings from the Upwork GraphQL API. It allows you to search for job listings based on a search term and returns detailed information about the jobs, such as titles, descriptions, skills required, and client preferences.

## Features

- Search for jobs using a search term (default: "Python Developer").
- Specify the number of job results to fetch.
- Fetch job details, including title, description, skills required, budget, job type, and client information.

## Prerequisites

Before running the scraper, make sure you have the following:

- Python 3.x installed.
- Upwork API key and Access Token (you can generate these from your Upwork account).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/upwork-jobs-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd upwork-jobs-scraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Create a `.env` file in the root directory and add your Upwork API credentials:

   ```plaintext
   UPWORK_API_KEY=your_upwork_api_key
   UPWORK_ACCESS_TOKEN=your_access_token
   ```

## Usage

You can run the scraper with the following command:

```bash
python main.py -search "Search Term" -results <Number of Results>
```

- `-search`: The job search term. Default is `Python Developer`.
- `-results`: The number of results to fetch. Default is `10`.

### Example

To search for "Data Scientist" job postings and fetch 5 results:

```bash
python main.py -search "Data Scientist" -results 5
```

## Code Structure

- `main.py`: The main script that accepts arguments for the search term and result count, then fetches and prints job postings from the Upwork API.
- `utils/get_jobs.py`: Contains the `fetch_job_postings` function which sends the GraphQL query and fetches job postings from the Upwork API.
- `requirements.txt`: A list of required Python libraries.

## Example Response

An example of a job posting fetched from the Upwork API:

```json
{
  "id": "123456",
  "title": "Python Developer",
  "description": "Looking for an experienced Python developer...",
  "skills": [
    { "name": "Python" },
    { "name": "Django" }
  ],
  "budget": 1000,
  "jobType": "Fixed",
  "client": {
    "country": "United States",
    "rating": 4.8,
    "feedbackScore": 99
  }
}
```

## Error Handling

If an error occurs during the API request, an error message will be printed in the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
