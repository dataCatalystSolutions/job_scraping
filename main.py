from dotenv import dotenv_values
import argparse

from graphqlclient import GraphQLClient

from utils.get_jobs import fetch_job_postings

config = dotenv_values(".env")
api_key = config.get("UPWORK_API_KEY")
access_token = config.get("UPWORK_ACCESS_TOKEN")

client = GraphQLClient('https://www.upwork.com/ab/graphql')

parser = argparse.ArgumentParser(description='Upwork Jobs Scraper')
parser.add_argument('-search', type=str, default='Python Developer', help='Search Term')
parser.add_argument('-results', type=int, default=10, help='Result Count')
args = parser.parse_args()

search_term = args.search
result_count = args.results

job_postings = fetch_job_postings(client=client,
                                  search_term=search_term,
                                  result_count=result_count,
                                  access_token=access_token,
                                  api_key=api_key)
print(search_term)
print(result_count)
