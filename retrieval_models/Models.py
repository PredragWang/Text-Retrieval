from math import log,pow
"""
-------------------------------------------------------------------------------
About: library of Retrieval Models
Author: Guanyu Wang
Date: 3-24-2016
-------------------------------------------------------------------------------
"""

def get_okapi (tf, doc_len, avglen):
    okapi = tf/(tf + 0.5 + 1.5*(doc_len/avglen))
    return okapi

def get_okapi_score(use_idf, query, doc, avg_len, avg_q_len):
  score = 0.0
  wordsInDoc = doc.getWordsCount()
  wordsInQuery = query.getWordsCount()
  for term, query_tf in wordsInQuery.iteritems():
    tf = WordsCountDoc.get(term)
    if tf == None: tf = 0
    if use_idf:
      idf = idf_list[nth_term]
      idf_query = df_q.get(query_terms[nth_term])
      idf_query = log(total_q/float(idf_query),2)
    else:
      idf = 1
      idf_query = 1
    temp1 = idf * get_okapi(tf, doc.getDocLen(), avg_len)
    temp2 = idf_query * get_okapi(query_tf, query.getDocLen(), avg_q_len)
    score += temp1*temp2
  return score  
                 
def laplace_smoothing(query, doc):
    score = 0.0
    wordsInDoc = doc.getWordsCount()
    wordsInQuery = query.getWordsCount()
    doc_len = doc.getDocLen() 
    tf_list = []
    for term,query_tf in wordsInQuery.iteritems():
      tf = wordsInDoc.get(term)
      if tf == None: tf = float(0)
      tf_list.append(tf)
      score += log(math.pow((tf_list[i] + 1)/(float(doc_len) + float(k)), float(query_tf)))
    return score