import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine(
	'postgresql://{}:{}@{}:{}/{}'.format(
		os.environ.get('POSTGRES_USER'),
		os.environ.get('POSTGRES_PASSWORD'),
		os.environ.get('POSTGRES_HOST'),
		os.environ.get('POSTGRES_PORT'),
		os.environ.get('POSTGRES_DB')
	)
)
pd.read_csv('movies.csv')[
	['imdb_id', 'original_title', 'overview']
].dropna().to_sql('movies_app_movie', con=engine, if_exists="append", index=False)
