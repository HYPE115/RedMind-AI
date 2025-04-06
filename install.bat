@ echo off
color 2
python -m pip install --upgrade pip
pip install llama-cpp-python flask chromadb langchain PyPDF2 markdown
pip3 install huggingface-hub
huggingface-cli download TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
pause
