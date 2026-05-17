import os
from pypdf import PdfReader

def local_pdf_rag(query: str) -> str:
    """دالة محلية لقراءة المراجع من فولدر knowledge_base وفلترتها بحسب السؤال"""
    folder_path = 'knowledge_base'
    if not os.path.exists(folder_path):
        return "Warning: 'knowledge_base' folder not found. No local PDF context provided."
        
    extracted_text = ""
    try:
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
        if not pdf_files:
            return "Warning: No PDF files found in 'knowledge_base'."
            
        for file_name in pdf_files:
            file_path = os.path.join(folder_path, file_name)
            reader = PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += f"[{file_name}] " + text + "\n"
                    
        keywords = query.split()
        relevant_lines = []
        for line in extracted_text.split('\n'):
            if any(keyword.lower() in line.lower() for keyword in keywords):
                relevant_lines.append(line)
                
        if len(relevant_lines) > 0:
            return "\n".join(relevant_lines[:50])
        else:
            return extracted_text[:4000]
    except Exception as e:
        return f"Error reading PDFs: {str(e)}"

def get_or_create_student_memory(student_id: str, new_log: str = None) -> str:
    """نظام الذاكرة المتقدمة وحفظ ملف الطالب محلياً"""
    memory_file = f"memory_{student_id}.txt"
    if new_log:
        with open(memory_file, "a", encoding="utf-8") as f:
            f.write(new_log + "\n")
            
    if os.path.exists(memory_file):
        with open(memory_file, "r", encoding="utf-8") as f:
            return f.read()
    return "No previous interaction history for this student. First session."