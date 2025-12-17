import pandas as pd

df = pd.read_csv("transactions_dirty.csv")

# Supprimer les lignes avec user_id non numérique
df = df[pd.to_numeric(df['user_id'], errors='coerce').notnull()]
df['user_id'] = df['user_id'].astype(int)

def convert_amount(x):
    try:
        return float(x)
    except:
        try:
            return float(w2n.word_to_num(str(x)))
        except:
            return None

df['amount'] = df['amount'].apply(convert_amount)

# Convertir timestamp en datetime et supprimer les lignes invalides
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp'])

# Supprimer les doublons
df = df.drop_duplicates()

# Réinitialiser l'index
df = df.reset_index(drop=True)

print(df)
