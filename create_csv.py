import pandas as pd
import os

# Folder where all the Parquet files are stored
parquet_folder = 'C:/Users/Admin/Desktop/ai creater/data/japanese-anime-speech/data'
parquet_files = [f for f in os.listdir(parquet_folder) if f.endswith('.parquet')]

# Load and concatenate all Parquet files into a single DataFrame
df_list = [pd.read_parquet(os.path.join(parquet_folder, f)) for f in parquet_files]
df_parquet = pd.concat(df_list, ignore_index=True)

# Load the transcription text file
with open('C:/Users/Admin/Desktop/ai creater/data/japanese-anime-speech/audio_transcription_list.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Create a DataFrame from the transcription file
transcription_data = [line.strip().split('|') for line in lines]
df_transcription = pd.DataFrame(transcription_data, columns=['audio_file', 'transcription'])

print(df_parquet['audio'].head())
print(df_transcription['audio_file'].head())

df_parquet['audio'] = df_parquet['audio'].apply(lambda x: str(x) if isinstance(x, dict) else x)
df_transcription['audio_file'] = df_transcription['audio_file'].apply(lambda x: str(x) if isinstance(x, dict) else x)


# Merge Parquet and transcription data on the audio file name
df_merged = pd.merge(df_parquet, df_transcription, left_on='audio', right_on='audio_file', how='inner')

# Save the merged data to a CSV file
df_merged.to_csv('output_combined.csv', index=False)

print("CSV file created successfully.")