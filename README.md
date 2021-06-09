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
Skrypty usprawniające pracę z silnikami również znajdują się w repozytorium w folderze [scripts](https://github.com/martynapawlus/PolishSpeechRecognition/tree/main/scripts). 😸
4. Obliczenie **Word Error Rate (WER)** przy użyciu programu [sclite](https://github.com/usnistgov/SCTK).
5. Przygotowanie pliku [.csv](https://github.com/martynapawlus/PolishSpeechRecognition/tree/main/wyniki) zawierającego w kolumnach wszystkie cechy poszczególnych tekstów i nagrań. 
6. Analiza wyników w środowisku R.
