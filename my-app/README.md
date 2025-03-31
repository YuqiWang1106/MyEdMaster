Opeartion Logic

------ Front End Start ------
1. `cd my-app`
2. `npm install`
3. `npm start`


------ Back End Start ------
!!! Please use virtual environment (venv) to run the backend
1. `cd server`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload`


----- Operation Logic ------
1. In the front end, input the topics, facts, strategies, procedures, rationales
2. Send these five contents to backend by clicking the submit button
3. Backend get the topics and pass to the LLM prompt
4. Backend use LLM to generate the facts, strategies, procedures, rationales
5. Backend get facts, stratgies, procedures, rationales both from user and LLM
6. Backend embeds one pair of them (user's facts & LLM's facts)
7. Backend comapre the similarity of this pair using the method of consine similarity 
8. Print this similarity
9. Repeate step 6-8 with each pair of them (facts & strategies & procedures & rationales)


----- Models Used -------
1. LLM: gpt-4o-2024-08-06
2. Embedding: text-embedding-ada-002