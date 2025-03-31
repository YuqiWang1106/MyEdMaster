import os
import json
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EXAMPLE_PROMPT = """
I want to teach you how to assess your own knowledge that you have about a subject area.
Let’s do this by taking an example that you already know.

Suppose you wanted to assess your own knowledge about solving 2-step equations of the form ax + b = c.
An example of this type of problem is 2x + 3 = 15.

If I want to be able to solve problems like these, I need four types of knowledge:
- Facts
- Strategies
- Procedures
- Rationales

Facts are concepts you have that describe objects or elements.
For example, for two-step equations, I need to know what variables, constants, coefficients, equations, and expressions are.

Strategies are general processes I would use to solve a problem.
For two-step equations, this would be reverse order of operations.

Procedures are the specific steps that I would use in a strategy.
So if I am using reverse order of operations, I need to know additive and multiplicative inverses.

Finally, rationales are the reasons why the strategies or the procedures work the way they do.
This could include things like the subtraction or the division property of equality.

You can think of:
- Facts as telling you “what”
- Strategies and Procedures as telling you “how”
- Rationales as telling you “why”

Here is a complete example based on the topic "Solving 2-step equations":

Facts:
I need to know what variables, constants, coefficients, equations and expressions are. A variable is an unknown quantity, usually represented by a letter. A constant is a specific number. A coefficient is a number that you multiply a variable by like 2x. An equation is an expression that is equal to another expression and joined by an equal sign. An expression is one or more terms that are combined by mathematical operations like addition, subtraction, multiplication and division.

Strategies:
I need to know reverse order of operations which is SADMEP. This stands for subtraction, addition, division, multiplication, exponents and parentheses. I know that I’m supposed to do these in order but I don’t remember whether I’m supposed to do subtraction always before addition or just which one goes first. The same is true for division and multiplication.

Procedures:
I need to know additive inverse and multiplicative inverse. The additive inverse is taking the number with the opposite sign as the constant and adding it to both sides of the equation. The multiplicative inverse is taking the inverse of the coefficient of the variable and multiplying both sides of the equation by it.

Rationales:
The subtraction property of equality says that if I subtract the same number from both sides, I preserve the equality. The division property of equality says that if I divide both sides of the equation by the same number, I preserve the equality.

---

Now, based on the new topic: "{topic}", generate a new self-assessment response with the following fields:
- facts
- strategies
- procedures
- rationales

Format the output as a JSON object like this:

{
  "facts": "...",
  "strategies": "...",
  "procedures": "...",
  "rationales": "..."
}
"""

async def generate_self_assessment(topic: str):
    prompt = EXAMPLE_PROMPT.replace("{topic}", topic)
    
    response = client.responses.create(
        model="gpt-4o-2024-08-06",
        input=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates structured JSON self-assessment content based on a math topic."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "self_assessment_generation",
                "schema": {
                    "type": "object",
                    "properties": {
                        "facts": {"type": "string"},
                        "strategies": {"type": "string"},
                        "procedures": {"type": "string"},
                        "rationales": {"type": "string"}
                    },
                    "required": ["facts", "strategies", "procedures", "rationales"],
                    "additionalProperties": False
                },
                "strict": True
            }
        }
    )
    
    result = json.loads(response.output_text)

    facts = result["facts"]
    strategies = result["strategies"]
    procedures = result["procedures"]
    rationales = result["rationales"]


    print(f"Topic: {topic}")
    print("\nFacts:\n", facts)
    print("\nStrategies:\n", strategies)
    print("\nProcedures:\n", procedures)
    print("\nRationales:\n", rationales)
    print("================================\n")

    return result


def get_embedding(text: str, model: str = "text-embedding-ada-002") -> np.ndarray:
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return np.array(response.data[0].embedding)

def cosine_similarity(vec1, vec2):
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))