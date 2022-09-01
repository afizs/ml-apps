from config import api_key
import oneai

oneai.api_key = api_key

def html_to_summary(url:str) -> str:
  pipeline = oneai.Pipeline(
    steps = [
      oneai.skills.HtmlToArticle(), 
      oneai.skills.Summarize()
    ]
  )
  output = pipeline.run(url)
  return output.html_article.summary.text

if __name__ == '__main__':
  with open('data.txt') as f:
    for idx, url in enumerate(f.readlines()):
      print(f'{idx+1} >> {url}\n')
      print(html_to_summary(str(url).strip()))
      print('\n')