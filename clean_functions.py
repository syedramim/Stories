from datetime import datetime
from textblob import TextBlob
import re 
import textstat

def calculate_downvotes(upvotes, upvote_ratio):
      return round(upvotes/upvote_ratio - upvotes)

def convert_to_time(string):
      return datetime.strptime(string, "%H:%M")

def handle_date(created_time):
      dt = datetime.fromtimestamp(created_time)
      
      date = f"{str(dt.month).zfill(2)}-{str(dt.day).zfill(2)}-{dt.year}"
      time_of_day = convert_to_time(dt.strftime("%H:%M"))
      
      if convert_to_time("00:00") <= time_of_day <= convert_to_time("04:59"):
            time_of_day = "Midnight"
      elif convert_to_time("05:00") < time_of_day < convert_to_time("05:59"):
            time_of_day = "Dawn"
      elif convert_to_time("06:00") < time_of_day < convert_to_time("11:59"):
            time_of_day = "Morning"
      elif convert_to_time("12:00") < time_of_day < convert_to_time("12:59"):
            time_of_day = "Noon"
      elif convert_to_time("13:00") < time_of_day < convert_to_time("16:59"):
            time_of_day = "Afternoon"
      elif convert_to_time("17:00") < time_of_day < convert_to_time("18:59"):
            time_of_day = "Evening"
      else:
            time_of_day = "Night"

      return {"date": date, "time_of_day": time_of_day}

def get_word_list(string) -> str:
      return re.findall(r"\b\w[\w'-]*\b", str(string))

def divider(num1, num2):
      return num1 / num2 if num2 > 0 else 0

def get_avg_word_length(arr):
      return divider(sum(len(word) for word in arr), len(arr))

def get_sentences(string):
      return TextBlob(string).sentences

def get_sentiment(string):
      return TextBlob(string).sentiment

def get_syllable_count(string):
      return textstat.syllable_count(string)

def get_reading_score(string):
      return textstat.flesch_reading_ease(string)

def get_reading_grade(string):
      return textstat.text_standard(string)

def get_story_sent_info(sentences):
      amount_sent = len(sentences)
      words_in_sent = 0
      syllables_in_sent = 0
      polarity_sentences = 0
      subjectivity_sentences = 0
      reading_score_sentences = 0
      
      for sentence in sentences:
            sent = str(sentence)
            sentiment = get_sentiment(sent)
            words_in_sent += len(get_word_list(sent))
            syllables_in_sent += get_syllable_count(sent)
            polarity_sentences += sentiment.polarity
            subjectivity_sentences += sentiment.subjectivity
            reading_score_sentences += get_reading_score(sent)
      
      return {
            "amount_sentences": len(sentences),
            "avg_words_per_sentence": divider(words_in_sent, amount_sent),
            "avg_syllables_per_sentence": divider(syllables_in_sent, amount_sent),
            "avg_polarity_per_sentence": divider(polarity_sentences, amount_sent),
            "avg_subjectivity_per_sentence": divider(subjectivity_sentences, amount_sent),
            "avg_readscore_per_sentence": divider(reading_score_sentences, amount_sent)
      } 

def info(string, isTitle):
      words = get_word_list(string)
      name = 'title' if isTitle else 'story'
      
      result =  {
            f'{name}_length': len(string),
            f'{name}_word_count': len(words),
            f'{name}_avg_word_length': get_avg_word_length(words),
            f'{name}_syllables': get_syllable_count(string),
            f'{name}_reading_score': get_reading_score(string),
            f'{name}_reading_grade': get_reading_grade(string),
            f'{name}_polarity': round(get_sentiment(string).polarity, 3),
            f'{name}_subjectivity': round(get_sentiment(string).subjectivity, 3)     
      }
      
      if not isTitle:
        result.update(get_story_sent_info(get_sentences(string)))
      
      return result