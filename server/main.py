# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai_service import generate_self_assessment
import numpy as np
import openai
from openai_service import generate_self_assessment, get_embedding, cosine_similarity

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    topic = data.get("topic", "")


# User Inputs (4 parts)
    user_data = data.get("user", {})
    user_facts = user_data.get("facts", "")
    user_strategies = user_data.get("strategies", "")
    user_procedures = user_data.get("procedures", "")
    user_rationales = user_data.get("rationales", "")
    
# LLM Results (4 parts)
    llm_result = await generate_self_assessment(topic)
    llm_facts = llm_result.get("facts", "")
    llm_strategies = llm_result.get("strategies", "")
    llm_procedures = llm_result.get("procedures", "")
    llm_rationales = llm_result.get("rationales", "")
    
    
    def compute_similarity(user_text, llm_text):
        # Embed user and LLM Results
        user_emb = get_embedding(user_text)
        llm_emb = get_embedding(llm_text)
        # Calculate the similarity
        return cosine_similarity(user_emb, llm_emb)
    
    sim_facts = compute_similarity(user_facts, llm_facts)
    sim_strategies = compute_similarity(user_strategies, llm_strategies)
    sim_procedures = compute_similarity(user_procedures, llm_procedures)
    sim_rationales = compute_similarity(user_rationales, llm_rationales)
    
    print(f"\n===== Similarity Scores for Topic: {topic} =====")
    print("Facts Similarity:", sim_facts)
    print("Strategies Similarity:", sim_strategies)
    print("Procedures Similarity:", sim_procedures)
    print("Rationales Similarity:", sim_rationales)
    print("============================================\n")
    
    return {

    }