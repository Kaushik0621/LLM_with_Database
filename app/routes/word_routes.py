from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.openai_client import get_meaning_from_gemai

router = APIRouter()

@router.get("/meaning/{word}")
def get_meaning(word: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT meaning FROM dictionary WHERE word = ?", (word,))
    result = cursor.fetchone()

    if result:
        return {"word": word, "meaning": result["meaning"]}
    else:
        meaning = get_meaning_from_gemai(word)
        cursor.execute("INSERT INTO dictionary (word, meaning) VALUES (?, ?)", (word, meaning))
        conn.commit()
        conn.close()
        return {"word": word, "meaning": meaning}

@router.get("/whole-dictionary")
def get_whole_dictionary():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT word, meaning FROM dictionary")
    results = cursor.fetchall()

    dictionary = [{"word": row["word"], "meaning": row["meaning"]} for row in results]
    conn.close()
    return dictionary
