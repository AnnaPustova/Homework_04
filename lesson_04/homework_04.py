adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3


""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

task_01 = adwentures_of_tom_sawer.replace("\n", " ")

print("1) ", task_01)

""" Замініть .... на пробіл
"""
task_02 = adwentures_of_tom_sawer.replace("....", " ")

print("2) ", task_02)

""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
task_03 = ' '.join(adwentures_of_tom_sawer.split())

print("3) ", task_03)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
task_04 = adwentures_of_tom_sawer.count("h")

print("4) ", task_04)
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()

capitalized_words_count = sum(1 for word in words if word[0].isupper())

print("5) ", capitalized_words_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_occurrence = adwentures_of_tom_sawer.find('Tom')

second_occurrence = adwentures_of_tom_sawer.find('Tom', first_occurrence + 1)

print("6) ", second_occurrence)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#понятие не имею как это решить)

adwentures_of_tom_sawer_sentences= adwentures_of_tom_sawer.split(".")
print("7) ",adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

task_08 = adwentures_of_tom_sawer_sentences[3].strip().lower()

print("8) ", task_08)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print('9) Yes, there is a sentence that starts with \'By the time\'.')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].split()

num_words_last_sentence = len(last_sentence_words)

print("10) ", num_words_last_sentence)
