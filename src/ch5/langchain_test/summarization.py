from langchain.docstore.document import Document
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain

# 直接APIキーを指定する場合、以下↓に指定する
# os.environ["OPENAI_API_KEY"] = 'xxx'

# 要約したいテキストファイル --- (*1)
target_text_file = './wikipedia_ai.txt'

# テキストファイルを読む --- (*2)
with open(target_text_file, 'rt', encoding='UTF-8') as f:
    long_text = f.read()

# 大規模言語モデルを用意する --- (*3)
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

# 長文テキストを意味のあるまとまりで分割する --- (*4)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600, # 分割サイズ
    chunk_overlap=0) # オーバーラップする文字数
texts = text_splitter.split_text(long_text)

# ドキュメントに変換する --- (*5)
docs = [Document(page_content=t) for t in texts]

# 要約のためのプロンプトを用意(日本語で要約するように指示) --- (*6)
template = '''Write a concise summary of the following:
```
{text}
```
CONCISE SUMMARY IN JAPANESE:'''
prompt = PromptTemplate(template=template, input_variables=['text'])

# 要約を実行 --- (*7)
chain = load_summarize_chain(llm, 
            chain_type='map_reduce', # どのように要約を行うか
            map_prompt=prompt,  # テンプレートを適用
            combine_prompt=prompt, verbose=False)
short_text_obj = chain(
    {'input_documents': docs}, 
    return_only_outputs=True)

# 結果を表示
print('[要約]', short_text_obj)
