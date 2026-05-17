from crewai import Crew, Process
from config import setup_environment
from tools import local_pdf_rag, get_or_create_student_memory
from agents import create_educational_agents
from tasks import create_educational_tasks

# تفعيل الإعدادات والمفاتيح فور استدعاء الملف
setup_environment()

def run_advanced_educational_system(user_query, student_id, target_language="Arabic"):
    # 1. جلب سياق الذاكرة والـ RAG
    student_history = get_or_create_student_memory(student_id)
    pdf_context = local_pdf_rag(user_query)

    # 2. إنشاء الوكلاء والمهام من الموديولات الأخرى
    agents = create_educational_agents()
    tasks = create_educational_tasks(agents, user_query, pdf_context, student_history, target_language)

    # 3. تجميع وتشغيل الـ Crew بالتنسيق التتابعي
    educational_crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        memory=False,
        verbose=True
    )

    final_output = educational_crew.kickoff()
    
    # 4. تحديث الذاكرة محلياً بعد انتهاء التشغيل بنجاح
    get_or_create_student_memory(student_id, f"Learned about: {user_query}")
    
    return final_output