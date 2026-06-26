#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("tmdb_5000_movies.csv")
df
credits = pd.read_csv("tmdb_5000_credits.csv")


# In[2]:


df.head()
# df.tail()
# df.sample()
# df.describe()
# df.decribe(include = "all")


# In[3]:


df.nunique()


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.size


# In[7]:


df.columns


# In[8]:


df.dtypes


# In[9]:


df.isnull().sum()


# In[10]:


df = df.drop( columns = ["homepage","tagline"] ) 


# In[11]:


df = df.dropna( subset  = ["overview"])


# In[12]:


df.duplicated().sum()


# In[13]:


df.columns


# In[14]:


df["genres"].unique()


# In[15]:


df.iloc[2]


# In[16]:


df['genres'].iloc[0]


# In[17]:


df.iloc[1]


# In[18]:


type(df['genres'].iloc[0]
    )


# In[19]:


x = [{"id": 12, "name": "Adventure"}]


# In[20]:


x[0]


# In[21]:


x[0]['name']


# In[22]:


import ast


# In[23]:


sample =  (df['genres'].iloc[0])
converted = ast.literal_eval(sample)
print(converted)


# In[24]:


type(converted)


# In[25]:


converted[2]['name']


# In[26]:


for i in converted :
    print(i['name'])


# In[27]:


def convert(obj):
    L =[]
    for i in obj :
        L.append(i['name'])
    return L 


# In[28]:


convert(converted)


# In[29]:


df['genres'] = df['genres'].apply(ast.literal_eval)


# In[30]:


df['genres'] = df['genres'].apply(convert)


# In[31]:


df['genres'].iloc[18]


# In[32]:


type(df['keywords'].iloc[0])


# In[33]:


df['keywords'] = df['keywords'].apply(ast.literal_eval)


# In[34]:


df['keywords'] = df['keywords'].apply(convert)


# In[35]:


df['keywords'].iloc[0]


# In[36]:


(df['title'] == df['original_title']).sum()


# In[37]:


df[df['title'] != df['original_title']][['title','original_title']].head(5)


# In[38]:


df.isnull().sum()


# In[39]:


type(df['overview'].iloc[0])


# In[40]:


df.shape


# In[41]:


df['id'].nunique()


# In[42]:


df = df.merge(
    credits , left_on = 'id' , right_on = 'movie_id' ) 


# In[43]:


credits.columns


# In[44]:


df.shape


# In[45]:


df.size


# In[46]:


df.head()


# In[47]:


type(df['cast'].iloc[0])


# In[48]:


df['cast'].iloc[1]


# In[49]:


(df['title_x'] == df['title_y']).sum()


# In[50]:


df = df.drop(columns = ["title_y"])


# In[51]:


df['cast'] = df['cast'].apply(ast.literal_eval)


# In[52]:


df['cast'] = df['cast'].apply(convert)


# In[53]:


df['cast'].iloc[0]


# In[54]:


crew_sample = ast.literal_eval(df['crew'].iloc[0])
crew_sample[6]


# In[55]:


type(crew_sample)


# In[56]:


df['crew'].iloc[1]


# In[57]:


def top3(obj):
    return obj[:3]
df['cast'] = df['cast'].apply(top3)


# In[58]:


def fetch_director(obj):
    L = []
    for i in obj:
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L
# we have created a function which fetches my director in my 


# In[59]:


df['crew'] = df['crew'].apply(ast.literal_eval)


# In[60]:


df['crew'] = df['crew'].apply(fetch_director)


# In[61]:


type(df['crew'].iloc[0])


# In[62]:


df['crew'].iloc[0]


# In[63]:


type(df['overview'].iloc[0])


# In[64]:


df['overview'] = df['overview'].apply(lambda x: x.split())


# In[65]:


type(df["overview"].iloc[0])


# In[66]:


df['tags'] = (
    df['overview']
    + df['genres']
    + df['keywords']
    + df['cast']
    + df['crew']
)


# In[67]:


new_df = df[['id', 'title_x', 'tags']]


# In[68]:


new_df.rename(columns={'title_x':'title'}, inplace=True)


# In[69]:


new_df.head()


# In[70]:


new_df['tags'].iloc[0]


# In[71]:


new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))


# In[72]:


new_df['tags'].iloc[0]


# In[73]:


new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())


# In[74]:


new_df['tags'].iloc[0]


# In[76]:


from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


# In[77]:


def stem(text):
    L = []

    for i in text.split():
        L.append(ps.stem(i))

    return " ".join(L)


# In[78]:


new_df['tags'] = new_df['tags'].apply(stem)


# In[79]:


from sklearn.feature_extraction.text import CountVectorizer


# In[80]:


cv = CountVectorizer(max_features=5000, stop_words='english')


# In[81]:


vectors = cv.fit_transform(new_df['tags']).toarray()


# In[82]:


vectors.shape
#5000 are words/features 


# In[83]:


from sklearn.metrics.pairwise import cosine_similarity


# In[84]:


similarity = cosine_similarity(vectors)


# In[85]:


similarity.shape 


# In[86]:


def recommend(movie):
    movie = movie.lower()

    movie_index = new_df[new_df['title'].str.lower() == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)


# In[89]:


recommend("Spectre")


# In[90]:


import pickle

with open("movies.pkl", "wb") as f:
    pickle.dump(new_df, f)

with open("similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)


# In[ ]:




