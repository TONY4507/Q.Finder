def removeStopWords(recent_chat):
  stop_words = set(stopwords.words('english')+['?','what','how'])
  
  word_tokens = word_tokenize(recent_chat) 
  
  filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
  filtered_sentence = [] 
  
  for w in word_tokens: 
      if w not in stop_words: 
          filtered_sentence.append(w)
  #print(filtered_sentence)
  return filtered_sentence

def vectorizer(sent,m):
    vec=[]
    numw=0
    for w in sent:
        try:
            if numw==0:
                vec=m[w]
            else:
                vec=np.add(vec,m[w])
            numw+=1
        except:
            pass
        
    return np.asarray(vec)/numw

def makeClusters(chat_list):
  global final_clu
  m=Word2Vec(chat_list,size=50,min_count=1,sg=1)
  l=[]
  for i in chat_list:
    l.append(vectorizer(i,m))
  X=np.array(l)
  n_clusters=20
  clf=KMeans(n_clusters=n_clusters,max_iter=900,init='k-means++',n_init=1)
  labels = clf.fit_predict(X)
  
  clustered_data=[]
  for i in range(n_clusters):
    df=[str(stn).capitalize() for index,stn in enumerate(chat_list) if labels[index]==i]
    clustered_data.append(df)
    
 
 final_clu=clustered_data
