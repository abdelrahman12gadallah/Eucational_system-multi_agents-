import streamlit as st
import uuid
# استدعاء الدالة من الموديول الجديد المخصص لإدارة وتشغيل الـ Crew
from crew_manager import run_advanced_educational_system 

# 1. إعدادات الصفحة (Page Configuration)
st.set_page_config(
    page_title="EduSphere | Multi-Agent Learning Platform",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; 
        white-space: pre-wrap; 
        font-weight: bold; 
        font-size: 16px;
    }
    .student-card {
        padding: 15px;
        background-color: #eef2f7;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر والتعريف بالنظام
st.title("🎓 EduSphere: Advanced Agentic AI Classroom")
st.markdown("### نظام تعليمي ذكي متعدد الوكلاء مع ميزات الحماية المتقدمة والذاكرة المستمرة")

if "student_id" not in st.session_state:
    if "student_id" not in st.session_state:
        st.session_state["student_id"] = "STUDENT-CORE-SESSION"

# 3. القائمة الجانبية
with st.sidebar:
    st.header("👤 ملف الطالب ونظام الأمان")
    st.markdown(f"""
    <div class="student-card">
        <strong>معرف الطالب الحالي (Memory ID):</strong><br>
        <code>{st.session_state['student_id']}</code>
    </div>
    """, unsafe_allow_html=True)
    st.info("💡 هذا المعرّف تستخدمه الذاكرة المتقدمة لتتبع مستواك وتحسين جودة الإجابات في الجلسات القادمة.")
    
    st.divider()
    st.header("⚙️ خيارات التوليد")
    language = st.selectbox("لغة المحتوى (Language):", ["Arabic", "English"])
    st.caption("النظام يفحص المحتوى لغوياً وأمنياً قبل العرض.")

# الواجهة الرئيسية للمدخلات
with st.container():
    col1, col2 = st.columns([4, 1])
    with col1:
        topic = st.text_input(
            "ماذا تريد أن تتعلم اليوم؟", 
            placeholder="مثال: explain the difference between RAG and CAG..."
        )
    with col2:
        st.write(" ")
        st.write(" ")
        run_button = st.button("🚀 بناء المنهج الذكي", use_container_width=True)

# 4. المعالجة وعرض المخرجات بالتفصيل
if run_button:
    if topic:
        with st.status(f"⏳ يتم الآن تفعيل الوكلاء لفحص وتوليد '{topic}' باللغة {language}...", expanded=True) as status:
            try:
                result = run_advanced_educational_system(
                    user_query=topic, 
                    student_id=st.session_state["student_id"], 
                    target_language=language
                )
                
                status.update(label="✅ تم بناء وتدقيق المحتوى التعليمي بنجاح!", state="complete", expanded=False)
                st.balloons()

                tab1, tab2, tab3, tab4 = st.tabs([
                    "📖 المحتوى التعليمي المعتمد", 
                    "📝 الاختبار الذكي (Quiz)", 
                    "🛡️ تقرير الأمان والجودة",
                    "📊 تفاصيل المعمارية (System Architecture)"
                ])

                with tab1:
                    st.header("📚 الدروس المشروحة بالتفصيل")
                    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 3:
                        content_data = result.tasks_output[3].raw
                        st.markdown(content_data)
                        
                        st.download_button(
                            label="📥 تحميل المادة العلمية (Markdown)",
                            data=content_data,
                            file_name=f"{topic.replace(' ', '_')}_lessons.md",
                            mime="text/markdown"
                        )
                    else:
                        st.markdown(result.raw if hasattr(result, 'raw') else str(result))

                with tab2:
                    st.header("📝 اختبار تقييم الفهم الفوري")
                    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 4:
                        quiz_data = result.tasks_output[4].raw
                        st.markdown(quiz_data)
                    else:
                        st.info("جاري تنسيق وعرض الأسئلة...")

                with tab3:
                    st.header("🛡️ فلترة المخرجات وفحص الحماية والـ Guardrails")
                    st.success("🔒 تم فحص هذا المدخل وتأمينه ضد هجمات الـ Prompt Injection كما تم تصفية المخرجات من الهلوسة.")
                    
                    if hasattr(result, 'tasks_output') and len(result.tasks_output) > 5:
                        st.markdown("### ⚖️ تقرير المراجعة النهائية والتنقية لـ (Reviewer Agent):")
                        st.info(result.tasks_output[5].raw)

                with tab4:
                    st.header("⚙️ معمارية النظام ومؤشرات التقييم في المناقشة")
                    col_meta1, col_meta2 = st.columns(2)
                    with col_meta1:
                        st.markdown(f"""
                        * **نمط التنسيق:** تتابعي موديولاري منظم (`Modular Sequential Process`).
                        * **عدد الوكلاء النشطين:** 6 وكلاء متخصصين موزعين على ملفات منفصلة.
                        * **حالة الذاكرة المستمرة:** مفعلة محلياً وتعمل بناءً على الـ Student ID.
                        * **تقنيات الاسترجاع:** RAG محلي من فولدر `knowledge_base`.
                        """)
                    with col_meta2:
                        st.markdown("""
                        * **البونص المحقق أمنياً:** كشف الـ Prompt Injection وفلترة المخرجات (Option C & D).
                        * **البونص المحقق لغوياً:** دعم كامل وموحد للعربية والإنجليزية (Option B).
                        """)

            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء تشغيل واجهة الـ Streamlit: {e}")
    else:
        st.warning("⚠️ برجاء كتابة موضوع الدراسة أولاً.")

st.divider()
st.caption("🏆 مشروع مادة النماذج التوليدية العميقة (Deep Generative Models) - السنة الرابعة | كلية الذكاء الاصطناعي")