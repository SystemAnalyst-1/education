import pandas as pd

authors = pd.DataFrame({'author_id':[1, 2, 3],
                        'author_name':['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])

book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':[450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])

authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')

authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)

authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)

