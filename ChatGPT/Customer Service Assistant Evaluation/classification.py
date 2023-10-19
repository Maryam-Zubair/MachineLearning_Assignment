import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['API_KEY']
from products_data_english import products_data


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


delimiter = "####"
system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human

"""
def user_query(query):
    print(f"User query: {query}")
    messages =  [  
    {'role':'system', 
    'content': system_message},    
    {'role':'user', 
    'content': f"{delimiter}{query}{delimiter}"},  
    ] 
    response = get_completion_from_messages(messages)
    return response

def main():
    query1= "I want to unsubscribe from your service."
    response1= user_query(query1)
    print(f"System classification:\n {response1}")
    query2= "Tell me more about your flat screen tvs"
    response2= user_query(query2)
    print(f"System classification: \n {response2}")

if __name__ == "__main__":
    main()