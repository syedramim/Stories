from datetime import datetime
from textblob import TextBlob
import re 
import textstat

#Takes int-upvotes and float-upvote ration as input
#Uses formula upvotes/upvote_ratio - upvotes to calculate downvotes where upvotes/upvote_ratio = total_votes and so total_votes - upvotes = downvotes
#Returns float-downvotes
def calculate_downvotes(upvotes, upvote_ratio):
      return upvotes/upvote_ratio - upvotes

#Takes str-string as input
#Turns the date string into Hour:Minute format
#Returns datatime formmated HH:MM
def convert_to_time(string):
      return datetime.strptime(string, "%H:%M")

#Takes int-created_time
#Converts int to datetime assigns a date and time_of_day based of created_time
#Returns dict containing datetime-date and str-time_of_day
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

#Takes int-score as input
#Iterates through levels and checks which level score falls under
#Returns the str-level that the score is within
def get_fre_score_level(score):
      levels = [
            (30, 'Very Confusing'),
            (50, 'Difficult'),
            (60, 'Fairly Difficult'),
            (70, 'Standard'),
            (80, 'Fairly Easy'),
            (90, 'Easy'),
      ] 
    
      for threshold, level in levels:
        if score < threshold:
            return level
      
      return 'Very Easy'

#Takes a str-string as input
#Uses a regex expression to determine all the possible words
#Returns an array of all the possible words
def get_word_list(string):
      return re.findall(r"\b\w[\w'-]*\b", str(string))

#Takes int-num1 and int-num2 as input
#Divides num1 by num2 and makes sure no zero division error
#Returns float-division result otherwise int-0 if zero division error
def divider(num1, num2):
      return num1 / num2 if num2 > 0 else 0

#Takes array-arr as input
#Gets the sum of length of words in the arr and then divides by length of arr rouded to 3 decimals to give average word length in arr
#Returns float-average
def get_avg_word_length(arr):
      return round(divider(sum(len(word) for word in arr), len(arr)), 3)

#Takes str-string as input
#Uses the TextBlob library to get list of all sentences within string
#Returns array of all possible sentences
def get_sentences(string):
      return TextBlob(string).sentences

#Takes str-string as input
#Uses the TextBlob library to get sentiment score of string
#Returns sentiment score
def get_sentiment(string):
      return TextBlob(string).sentiment

#Takes str-string as input
#Uses the TextStat library to get the total syllables within string
#Returns int-amount of syllables
def get_syllable_count(string):
      return textstat.syllable_count(string)

#Takes str-string as input
#Uses the TextStat library to get the flesch_reading_ease score of the string
#Returns int-reading score of the string
def get_reading_score(string):
      return textstat.flesch_reading_ease(string)

#Takes str-string as input
#Uses the TextStat library to get the grade reading level of the string
#Returns str-grade reading level of the string
def get_reading_grade(string):
      return textstat.text_standard(string)

#Takes array-sentences as input
#Iterates through every sentence and calculates average metrics of all sentences by getting total metric divided by total sentences
#Returns dictionary with keys of amount_sentences, avg_words_per_sentence, avg_syllables_per_sentence, avg_polarity_per_sentence, avg_subjectivity_per_sentence, avg_readscore_per_sentence
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
            "avg_words_per_sentence": round(divider(words_in_sent, amount_sent), 3),
            "avg_syllables_per_sentence": round(divider(syllables_in_sent, amount_sent), 3),
            "avg_polarity_per_sentence": round(divider(polarity_sentences, amount_sent), 3),
            "avg_subjectivity_per_sentence": round(divider(subjectivity_sentences, amount_sent), 3),
            "avg_readscore_per_sentence": round(divider(reading_score_sentences, amount_sent), 3)
      } 

#Takes str-string and Bool-isTitle
#Given the string and whether or not it is a title, calculates metrics using helper functions
#Returns dictionary with keys of length, word_count, avg_word_length, syllable_count, reading metrics such as: score, grade, difficulty, the polarity and subjectivity, and sentence info if it is a story
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
            f'{name}_reading_difficulty': get_fre_score_level(get_reading_score(string)),
            f'{name}_polarity': round(get_sentiment(string).polarity, 3),
            f'{name}_subjectivity': round(get_sentiment(string).subjectivity, 3)     
      }
      
      if not isTitle:
        result.update(get_story_sent_info(get_sentences(string)))
      
      return result