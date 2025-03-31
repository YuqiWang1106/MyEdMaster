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


# 用户填写的四个部分
    user_data = data.get("user", {})
    user_facts = user_data.get("facts", "")
    user_strategies = user_data.get("strategies", "")
    user_procedures = user_data.get("procedures", "")
    user_rationales = user_data.get("rationales", "")
    
    # 调用 LLM 生成的评估
    llm_result = await generate_self_assessment(topic)
    llm_facts = llm_result.get("facts", "")
    llm_strategies = llm_result.get("strategies", "")
    llm_procedures = llm_result.get("procedures", "")
    llm_rationales = llm_result.get("rationales", "")
    
    # 定义比较函数
    def compute_similarity(user_text, llm_text):
        # 获取用户和 LLM 的文本嵌入
        user_emb = get_embedding(user_text)
        llm_emb = get_embedding(llm_text)
        return cosine_similarity(user_emb, llm_emb)
    
    sim_facts = compute_similarity(user_facts, llm_facts)
    sim_strategies = compute_similarity(user_strategies, llm_strategies)
    sim_procedures = compute_similarity(user_procedures, llm_procedures)
    sim_rationales = compute_similarity(user_rationales, llm_rationales)
    
    # 在后端打印相似度
    print(f"\n===== Similarity Scores for Topic: {topic} =====")
    print("Facts Similarity:", sim_facts)
    print("Strategies Similarity:", sim_strategies)
    print("Procedures Similarity:", sim_procedures)
    print("Rationales Similarity:", sim_rationales)
    print("============================================\n")
    
    # 返回相似度结果（如果需要传回前端，可以返回；否则也可以返回空字典）
    return {
        "similarities": {
            "facts": sim_facts,
            "strategies": sim_strategies,
            "procedures": sim_procedures,
            "rationales": sim_rationales
        }
    }