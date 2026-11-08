client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = "generate a product description for SonicPro headphones, including: 40-hour batter life and foldable design"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=100,
    temperature=2
)

print(response.choices[0].message.content)