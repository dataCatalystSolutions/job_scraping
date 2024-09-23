def fetch_job_postings(client, search_term, result_count, access_token, api_key):
    """

    :param client:
    :param search_term:
    :param result_count:
    :param access_token:
    :param api_key:
    :return:
    """

    query = f"""
    query {{
      jobs(query: "{search_term}", first: {result_count}) {{
        nodes {{
          id
          title
          description
          skills {{
            name
          }}
          budget
          jobType
          client {{
            country
            rating
            feedbackScore
          }}
        }}
      }}
    }}
    """

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Upwork-Api-Key': api_key,
        'Content-Type': 'application/json'
    }

    try:
        response = client.execute(query=query, headers=headers)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")