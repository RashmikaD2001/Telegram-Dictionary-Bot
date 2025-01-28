import requests

def get_word_meanings(word):
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    try:
        response = requests.get(base_url + word)
        if response.status_code == 200:
            data = response.json()
            meanings = data[0].get('meanings', [])
            
            result = []
            for meaning in meanings:
                part_of_speech = meaning.get('partOfSpeech', 'unknown')
                definitions = meaning.get('definitions', [])
                for definition in definitions:
                    result.append({
                        "partOfSpeech": part_of_speech,
                        "definition": definition.get('definition', ''),
                        "example": definition.get('example', 'No example provided.')
                    })
            return result
        else:
            return f"Error: Unable to fetch meaning for '{word}' (status code {response.status_code})"
    except Exception as e:
        return f"Error: {str(e)}"