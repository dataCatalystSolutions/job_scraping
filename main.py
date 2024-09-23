from dotenv import dotenv_values

from graphqlclient import GraphQLClient

from utils.get_jobs import fetch_job_postings

config = dotenv_values(".env")
api_key = config.get("UPWORK_API_KEY")
access_token = config.get("UPWORK_ACCESS_TOKEN")

client = GraphQLClient('https://www.upwork.com/ab/graphql')

search_term = "Python Developer"
result_count = 10

job_postings = fetch_job_postings(client=client,
                                  search_term=search_term,
                                  result_count=result_count,
                                  access_token=access_token,
                                  api_key=api_key)
print(job_postings)