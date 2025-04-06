from llama_cpp import Llama # type: ignore

llm = Llama(
    model_path="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
)

def get_response(prompt):
    formatted = f"""<|system|>Tu es RedMind AI, une intelligence artificielle experte en pentest et programmation. Quand on te pose une question, tu peux :
- Générer du code Python, Bash, C#, JavaScript...
- Donner des conseils de Red Team.
- Répondre comme un expert humain.
Réponds toujours avec précision et si possible avec du code clair, commenté, et efficace.<|end|><|user|>{prompt}<|end|><|assistant|>"""
    
    output = llm(formatted, max_tokens=1024, stop=["<|end|>"])
    return output["choices"][0]["text"].strip()