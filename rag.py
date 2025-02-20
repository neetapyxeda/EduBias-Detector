from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from openai import OpenAI

#os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
#os.environ["OPENAI_API_KEY"] =" "


MODEL="gpt-4o-mini"

# set the openai model
#llm = ChatOpenAI(model=MODEL, temperature=0)

# create client
#client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



#Function 
def extract_text_from_pdf(pdf_path):
    pdf_text = ""
    # read the pdf
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # extract the text
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_text += page.extract_text()

    final_text = pdf_text.strip().replace("\n", "")        
    return pdf_text





    