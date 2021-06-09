# TEST ROZPOZNAWANIA JĘZYKA POLSKIEGO
***by Martyna, Julia, Karolina***

Proces ma na celu zweryfikowanie ilościowej skuteczności działania silników rozpoznawania mowy w jęzku polskim, poprzez przeprowadzenie testów na zebranym zbiorze danych.
<br />Etapy przeprowadzania testów:
1. Przygotowanie nagrań (zarówno pobranych z internetu jak i nagranych) i podzielenie ich na sety. Wszystkie wykorzystane do testowania pliki audio znajdują się w repozytorium.
2. Opracowanie plików z transkrypcją do wykorzystania jako teksty referencyjne.
3. Przepuszczenie plików audio przez wybrane silniki rozpoznawania mowy.
    * [Google Cloud Platform](https://cloud.google.com/speech-to-text/docs/reference/rest/)
    * [Google Speech Recognition](https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancerecognize_googleaudio_data-audiodata-key-unionstr-none--none-language-str--en-us--pfilter-union0-1-show_all-bool--false---unionstr-dictstr-any)
    * [Azure](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text)
    * [Happyscribe](https://www.happyscribe.com/transcribe-polish)
    * [Sonix](https://sonix.ai/) <br />
*Pełne testy zostały przeprowadzone na wszystkich wyżej wymienionych z wyjątkiem Google Speech Recognition* <br />

Skrypty usprawniające pracę z silnikami również znajdują się w repozytorium w folderze [scripts](https://github.com/martynapawlus/PolishSpeechRecognition/tree/main/scripts).😸

4. Obliczenie **Word Error Rate (WER)** przy użyciu programu [sclite](https://github.com/usnistgov/SCTK).
5. Przygotowanie pliku [.csv](https://github.com/martynapawlus/PolishSpeechRecognition/tree/main/wyniki) zawierającego w kolumnach wszystkie cechy poszczególnych tekstów i nagrań. 
6. Analiza wyników w środowisku R.

### Podsumowanie
Oprócz wykorzystywanego narzędzia transkypcji, rozważany był wpływ następujących czynników:
  * dykcja
  * jakość mikrofonu
  * płeć
  * typ słownictwa
  * szum tła
  * szybkość mowy
<br /> <br />Najbardziej znaczącym z czynników okazała się dykcja oraz duży szum. <br />
<img src="https://github.com/martynapawlus/PolishSpeechRecognition/blob/main/wykresy/10.png" alt="ten" width="600"/>
W przypadku osób z dobrą dykcją średnia wartość WER wyniosła 19.11%, natomiast dla osób ze złą dykcją wartość ta była na poziomie 58.74% P-value dla tego testu osiągnęło wartość 2e-16, więc było bliskie zeru. Wpływ dykcji na odczyt WER okazał się niezaprzeczalny. Porównanie  grupy  osób  z  dobrą  oraz  przeciętną  dykcją  dostarczyło  spodziewanie  mniejszej  różnicy niż w przypadku powyższego zestawienia, ale nadal to transkrypcje osób z dobrą dykcją osiągnęły widocznie lepsze rezultaty. P-value w tym przypadku ma wartość 0.0121.Prawdopodobieństwo, że różnica między dwoma przedziałami jest zjawiskiem losowym jest więc bardzo małe.
<br />
<img src="https://github.com/martynapawlus/PolishSpeechRecognition/blob/main/wykresy/2.png" alt="two" width="650"/>
Duży szum okazał się mieć również nieprzypadkowy wpływ na wyniki WER, ponieważ w przypadku tego zestawienia wartość P-value wyniosła zaledwie 0.00146.

Pozostałe czynniki okazały się mało znaczące, a uzyskane wartości P-value sugerowały losowość wyników:
  * **Jakość mikrofonu** - różnica w wartościach WER między dobrym, a złym mikrofonem wynosiosła około 1 punkta procentowego. 
  * **Płeć** - różnica w wartościach WER dla lektorów różnych płci wyniosła 0.4 pp.
  * **Typ słownictwa** - tutaj rozbieżność wartości WER była nieco większa, bo ponad 2 pp, ale od strony statystycznej porównanie to nie ma dużego znaczenia.
  * **Mały szum tła** - różnica między małym szumem, a brakiem szumu była na poziomie ok. 1pp, więc wnioski nasuwają się same.

**Między poszczególnymi silnikami wystąpiły widoczne i nieprzypadkowe różnice w wartościach WER.**

<img src="https://github.com/martynapawlus/PolishSpeechRecognition/blob/main/wykresy/6.png" alt="two" width="700"/>

Do obliczeń potrzebnych do stworzenia tego zestawienia wykorzystane zostały wszystkie przygotowane nagrania, bez względu na badane czynniki, takie jak jakość mowy i mikrofonu. Każdy z silników przeprowadzał transkrypcję dokładnie takiego samego zestawu nagrań. Raport nie ujawnia nazw narzędzi, które uzyskały poszczególne wyniki. Prezentują się one natomiast następująco:
  * **Narzędzie 1** - średni WER: 23.47%
  * **Narzędzie 2** - średni WER: 30.30.38%
  * **Narzędzie 3** - średni WER: 36.31%
  * **Narzędzie 4** - średni WER: 34.83%

Co ciekawe, Google Speech Recognition (inne API), mimo tego, że teoretycznie korzysta z tego samego silnika, dało inne rezultaty niż Google Cloud Platform. Większość nagrań została przetranskrybowana nieco lepiej przy użyciu GSR.
<img src="https://github.com/martynapawlus/PolishSpeechRecognition/blob/main/wykresy/4.png" alt="two" width="600"/>

Średni WER dla Google Speech Recognition wyniósł - 17.72%, a dla Google Cloud Platform - 21.15%. Obliczenia te były przeprowadzone tylko dla części tekstów, ponieważ GSR nie podejmował próby transkrypcji nagrań, które charaktekryzowały się słabą dykcją lub dużym szumem. Zamiast tego wyrzucał błąd "UnknownValueError".

Testy, które wykonałyśmy dały satysfakcjonujące wyniki, zwłaszcza w kwestii prównania komercyjnych silników transkrypcji mowy.😺
